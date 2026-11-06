import	os
import	sys

import	requests
# import	urllib3

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8080")
TIMEOUT = 5

# urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
if sys.stdout.isatty() and "NO_COLOR" not in os.environ:
    GREEN, RED, BOLD, RESET = "\033[32m", "\033[31m", "\033[1m", "\033[0m"
else:
    GREEN = RED = BOLD = RESET = ""

fails = 0

def expect(expected, name, method, path, **kwargs):
    global fails
    try:
        r = requests.request(
            method, BASE_URL + path,
            timeout=TIMEOUT, verify=False, allow_redirects=False,
            **kwargs,
		)
        got = r.status_code
    except requests.RequestException as e:
        got = f"error ({type(e).__name__})"

    if got == expected:
        print(f"{GREEN}PASS{RESET} {name}")
    else:
        print(f"{RED}FAIL{RESET} {name} (expected {expected}, recived {got})")
        fails += 1

def finish():
    if fails == 0:
        print(f"{BOLD}{GREEN}Everything is OK !{RESET}")
    else:
        print(f"{BOLD}{RED}{fails} fail(s){RESET}")
    sys.exit(1)