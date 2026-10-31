// Offline support for the static site (GitHub Pages, or the app added to the home screen).
// Every page and quiz listed in offline.json is kept on the device; read-aloud audio only for the
// levels the learner saved from the home page (the page writes those files into the "audio" cache).
// The export fills in VERSION, so each deploy installs a new worker; unchanged files are copied over
// from the previous version instead of being downloaded again.
const VERSION = "__VERSION__";
const CACHE = "quiz-" + VERSION;
const AUDIO = "audio";
const BASE = new URL("./", self.location).href;

self.addEventListener("install", e => {
  self.skipWaiting();
  e.waitUntil(precache().catch(async err => {
    await caches.delete(CACHE);
    throw err;
  }));
});

self.addEventListener("activate", e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith("quiz-") && k !== CACHE) await caches.delete(k);
    await self.clients.claim();
  })());
});

async function broadcast(msg) {
  for (const c of await self.clients.matchAll({ includeUncontrolled: true })) c.postMessage(msg);
}

// The newest complete earlier version: { cache, files }.
async function previous() {
  for (const k of (await caches.keys()).reverse()) {
    if (!k.startsWith("quiz-") || k === CACHE) continue;
    const cache = await caches.open(k);
    const list = await cache.match(BASE + "offline.json");
    if (list && await cache.match(BASE + "__ready__")) return { cache, files: (await list.json()).files };
  }
  return null;
}

async function precache() {
  const res = await fetch(BASE + "offline.json", { cache: "no-store" });
  if (!res.ok) throw new Error("offline.json: " + res.status);
  const list = await res.json();
  const cache = await caches.open(CACHE);
  const old = await previous();
  const paths = Object.keys(list.files);
  const queue = paths.slice();
  let done = 0;
  const worker = async () => {
    while (queue.length) {
      const path = queue.shift();
      const url = BASE + path;
      let resp = old && old.files[path] === list.files[path] ? await old.cache.match(url) : null;
      if (!resp && !(await cache.match(url))) {
        resp = await fetch(url, { cache: "no-cache" });
        if (!resp.ok) throw new Error(path + ": " + resp.status);
      }
      if (resp) await cache.put(url, resp);
      if (++done % 20 === 0 || done === paths.length) broadcast({ type: "offline-progress", done, total: paths.length });
    }
  };
  await Promise.all(Array.from({ length: 6 }, worker));
  await cache.put(BASE + "offline.json", new Response(JSON.stringify(list)));
  await cache.put(BASE + "__ready__", new Response(VERSION));
  broadcast({ type: "offline-ready" });
}

// Audio elements ask for byte ranges (Safari always does); answer them from the cached file.
async function ranged(req, resp) {
  const range = req.headers.get("range");
  if (!range) return resp;
  const buf = await resp.arrayBuffer();
  const size = buf.byteLength;
  const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
  let start = 0, end = size - 1;
  if (m && m[1] !== "") { start = +m[1]; if (m[2] !== "") end = Math.min(+m[2], size - 1); }
  else if (m && m[2] !== "") start = Math.max(0, size - +m[2]);
  if (!m || start >= size || start > end) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
  }
  return new Response(buf.slice(start, end + 1), {
    status: 206,
    headers: {
      "Content-Type": resp.headers.get("Content-Type") || "audio/mpeg",
      "Content-Range": `bytes ${start}-${end}/${size}`,
      "Content-Length": String(end - start + 1),
      "Accept-Ranges": "bytes",
    },
  });
}

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET" || !req.url.startsWith(BASE)) return;
  const url = new URL(req.url);
  const rel = url.href.slice(BASE.length).split(/[?#]/)[0];
  if (rel.startsWith("audio/") && rel !== "audio/manifest.json") {
    e.respondWith((async () => {
      const hit = await caches.match(BASE + rel, { cacheName: AUDIO });
      return hit ? ranged(req, hit) : fetch(req);
    })());
    return;
  }
  const key = BASE + (rel === "" || rel.endsWith("/") ? rel + "index.html" : rel);
  e.respondWith((async () => {
    // match (not open) so that a worker being replaced doesn't re-create its deleted cache
    const hit = await caches.match(key, { cacheName: CACHE });
    if (hit) return hit;
    try {
      return await fetch(req);
    } catch (err) {
      // offline and not cached: open the quiz home rather than an error page
      const home = req.mode === "navigate" && await caches.match(BASE + "index.html");
      if (home) return home;
      throw err;
    }
  })());
});
