from lib import expect, finish

expect(200, "GET simple", "GET", "/get")
expect(200, "GET with parameters", "GET", "/get", params={"name": "value"})
expect(200, "GET with parameters", "GET", "/get", params={"ville": "Lyon"})
expect(200, "GET multi parametes", "GET", "/get", params={"jweber": "caca", "pde-petr": "pipi"})

expect(200, "POST form", "POST", "/post", data={"champ": "value"})
expect(200, "POST JSON", "POST", "/post", json={"a": 1})

expect(200, "Headers authorization", "GET", "/headers", headers={"Authorization": "Bearer abc123"})
expect(200, "Multi headers", "GET", "/headers", headers={"Authorization": "Bearer abc123", "X-Request-Id": "42", "Accept-Language": "fr-FR", "select":""})

expect(200, "Put", "PUT", "/put")

expect(200, "Delete", "DELETE", "/delete")

finish()