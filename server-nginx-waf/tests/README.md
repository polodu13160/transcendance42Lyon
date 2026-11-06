# Basic tests

```bash
python3 server-nginx-waf/tests/legit.py # everything must return 200
python3 server-nginx-waf/tests/attacks.py # everything must return 403
```
# WAFtester
### Install WAFtester
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install 22
nvm use 22
node -v
npm install -g @waftester/cli
```

### Use WAFtester
```bash
waf-tester vendor -u http://127.0.0.1:8080
waf-tester scan -u http://127.0.0.1:8080 --smart
```