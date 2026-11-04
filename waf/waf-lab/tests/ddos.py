from lib import expect, finish

for i in range(0, 1000):
    expect(200, "GET simple", "GET", "/get")

finish()