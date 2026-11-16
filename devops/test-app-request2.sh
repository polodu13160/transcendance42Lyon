#!/bin/bash

for i in $(seq 1 200); do
  curl -s localhost:8000/ > /dev/null
  # un POST de temps en temps (ici, 1 fois sur 10) :
done
