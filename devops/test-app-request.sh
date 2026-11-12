#!/bin/bash

for i in $(seq 1 200); do
  curl -s localhost:8000/ > /dev/null
  curl -s localhost:8000/games/$i > /dev/null
  curl -s localhost:8000/cacaprout > /dev/null
  # un POST de temps en temps (ici, 1 fois sur 10) :
  if [ $((i % 10)) -eq 0 ]; then
    curl -s -X POST "localhost:8000/games?mode=solo" > /dev/null
    curl -X POST "localhost:8000/join" > /dev/null
    curl -X POST "localhost:8000/matchmaking" > /dev/null
  fi
  if [ $((i % 10)) -eq 3 ]; then
    curl -X POST "localhost:8000/left" > /dev/null
  fi
done
