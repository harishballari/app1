import requests
import  json

url = 'http://127.0.0.1:8000/'

req1 =requests.get(url=url)

data =req1.json()

print(data)