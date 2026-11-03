#!/usr/bin/env bash

BASE_URL="${BASE_URL:-http://127.0.0.1:8080}"
FAILS=0

if [ -t 1 ] && [ -z "${NO_COLOR:-}" ]; then
    GREEN=$'\033[32m'
    RED=$'\033[31m'
    BOLD=$'\033[1m'
    RESET=$'\033[0m'
else
    GREEN="" RED="" BOLD="" RESET=""
fi

expect() {
    local expected="$1" name="$2"
    shift 2
    local got
    got=$(curl -s -o /dev/null -w '%{http_code}' "$@")
    if [ "$got" = "$expected" ]; then
        echo "${GREEN}PASS${RESET} $name"
    else
        echo "${RED}FAIL${RESET} $name (expected $expected, recived $got)"
        FAILS=$((FAILS + 1))
    fi
}

finish() {
    if [ "$FAILS" -eq 0 ]; then
        echo "${BOLD}${GREEN}Everything is OK !${RESET}"
        exit 0
    fi
    echo "${BOLD}${RED}$FAILS fail(s)${RESET}"
    exit 1
}