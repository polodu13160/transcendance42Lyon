#!/usr/bin/env bash
source "$(dirname "$0")/lib.sh"

expect 403 "SQL Injection" -i -G "$BASE_URL/get" --data-urlencode "id=1' OR '1'='1"

expect 403 "SQL Injection" -i -G "$BASE_URL/get" --data-urlencode "?id=1' OR '1'='1"

expect 403 "XSS Attack" -i -G "$BASE_URL/get" --data-urlencode "q=<script>alert(1)</script>"

expect 403 "Path trasversal" -i -G "$BASE_URL/get" --data-urlencode "?file=../../etc/passwc"

expect 403 "Command Injection" -i -G "$BASE_URL/get" --data-urlencode "?cmd=;cat/etc/passwd"

expect 403 "Scanner" -i -G "$BASE_URL/get" --data-urlencode "User-Agent: sqlmap"

# expect 403 "Protocol" -i -G "$BASE_URL/get" --data-urlencode ""

finish