#!/usr/bin/env bash

BASE_URL="${BASE_URL:-http://127.0.0.1:8080}"
FAILS=0


expect() {
    local expected="$1" name="$2"
    shift 2
    local got
    got=$(curl -s -o /dev/null -w '%{http_code}' "$@")
    if [ "$got" = "$expected" ]; then
        echo "PASS $name"
    else
        echo "FAIL $name (expected $expected, recived $got)"
        FAILS=$((FAILS + 1))
    fi
}

finish() {
    if [ "$FAILS" -eq 0 ]; then
        echo "Everything is OK !"
        exit 0
    fi
    echo "$FAILS fail(s)"
    exit 1
}