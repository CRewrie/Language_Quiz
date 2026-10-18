-- Progress sync for signed-in users. Run once in the Supabase SQL editor.
-- One row per user and key ("best", "srs", "progress"); the page merges it with its localStorage.

create table if not exists public.progress (
  user_id    uuid        not null default auth.uid() references auth.users (id) on delete cascade,
  key        text        not null check (key in ('best', 'srs', 'progress')),
  value      jsonb       not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, key)
);

alter table public.progress enable row level security;

-- New tables are not exposed automatically in this project: allow signed-in users only.
revoke all on public.progress from anon, authenticated;
grant select, insert, update, delete on public.progress to authenticated;

-- Everyone sees and changes only their own rows.
drop policy if exists "own rows: read" on public.progress;
drop policy if exists "own rows: insert" on public.progress;
drop policy if exists "own rows: update" on public.progress;
drop policy if exists "own rows: delete" on public.progress;
create policy "own rows: read"   on public.progress for select to authenticated using ((select auth.uid()) = user_id);
create policy "own rows: insert" on public.progress for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "own rows: update" on public.progress for update to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "own rows: delete" on public.progress for delete to authenticated using ((select auth.uid()) = user_id);
