#!/usr/bin/env bash
source "$(dirname "$0")/lib.sh"

expect 200 "GET simple" "$BASE_URL/get"

expect 200 "GET with parameters" -G "$BASE_URL/get" --data-urlencode "name=value"

expect 200 "GET with parameters" -G "$BASE_URL/get" --data-urlencode "ville=Lyon"

expect 200 "GET multi parameters" -G "$BASE_URL/get" --data-urlencode "jweber=caca" --data-urlencode "pde-petr=pipi"

expect 200 "POST form" -X POST "$BASE_URL/post" -d "champ=value"

expect 200 "POST JSON" -X POST "$BASE_URL/post" -H "Content-Type: application/json" -d '{"a":1}'

expect 200 "Headers authorization" -H "Authorization: Bearer abc123" "$BASE_URL/headers"

expect 200 "Multi headers" \
    -H "Authorization: Bearer abc123"\
    -H "X-Request-Id: 42" \
    -H "Accept-Language: fr-FR" \
    -H "select" \
    "$BASE_URL/headers"

expect 200 "Put" -X PUT "$BASE_URL/put"

expect 200 "Delete" -X DELETE "$BASE_URL/delete"

finish