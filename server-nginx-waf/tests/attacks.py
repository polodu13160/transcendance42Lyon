from lib import expect, finish

expect(403, "SQL Injection", "GET", "/get", params={"id": "1' OR '1'='1"})

expect(403, "SQL Injection", "GET", "/get", params={"?id": "1' OR '1'='1"})

expect(403, "XSS Attack", "GET", "/get", params={"q": "<script>alert(1)</script>"})

expect(403, "Path trasversal", "GET", "/get", params={"?file": "../../etc/passwc"})

expect(403, "Command Injection", "GET", "/get", params={"?cmd": ";cat/etc/passwd"})

expect(403, "Scanner", "GET", "/get", params={"User-Agent": "sqlmap"})


finish()