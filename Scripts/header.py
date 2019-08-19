#Imports the request package
import requests

#Url of the target
url = "http://httpbin.org/headers"

#Get the full page onto r
r = requests.get(url)

#Print the status code from r
print(r.status_code)

#Print just the headers from r
print(r.headers)

#Modify the User-Agent in the header
headers = {
   'User-Agent' :"Mobile"
}

#Request just the header again with the modified User-Agent
rh = requests.get(url,headers=headers)

#Print modifed header
print(rh.text)