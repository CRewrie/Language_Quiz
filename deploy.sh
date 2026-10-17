#!/bin/sh
# Deploy the quiz app to the home server "hive" (192.168.88.10).
# The Mac can't reach the server directly (Wi-Fi → LAN issue on the router),
# so SSH hops through the router; it asks for the router's root password.
set -e
cd "$(dirname "$0")"
JUMP="root@192.168.88.1"
HOST="constantin@192.168.88.10"
SSH="ssh -J $JUMP"

rsync -az --delete -e "$SSH" \
  --include=Cargo.toml --include=Cargo.lock --include=README.md \
  --include='src/***' --include='static/***' --include='quizzes/***' --exclude='*' \
  ./ "$HOST":japanese-quiz/

$SSH "$HOST" '
  set -e
  cd japanese-quiz
  cargo build --release 2>&1 | tail -1
  sudo install -m 755 target/release/japanese_quiz /opt/japanese-quiz/japanese_quiz
  sudo rm -rf /opt/japanese-quiz/quizzes
  sudo cp -r quizzes /opt/japanese-quiz/quizzes
  sudo chmod -R a+rX /opt/japanese-quiz/quizzes
  sudo systemctl restart japanese-quiz
  sleep 1
  journalctl -u japanese-quiz -n 1 --no-pager -o cat | head -1
  systemctl is-active japanese-quiz
'
