import requests
import json

with open(r"C:\Users\Playdata\Desktop\kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v1/api/talk/friends"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())