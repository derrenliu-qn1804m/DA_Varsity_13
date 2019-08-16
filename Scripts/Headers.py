import requests
headers = {
    'User-Agent': ‘Mobile’
}
req = requests.get("http://172.18.58.238/index.php")

print(req.status_code)
for x in req.headers:
    print("\t",x,":",req.headers[x])
