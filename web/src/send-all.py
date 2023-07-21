import requests
import json

with open(r"C:\Users\Playdata\Desktop\kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "receiver_uuids": '["yv7I8MbzyvvX5dDg0uXU5dH9xPfO-8n-iA"]',
    "template_object": json.dumps({
        "object_type":"text",
        "text":"야옹이가 위험물에 충돌했어요!",
        "link":{
            "web_url":"https://www.lksee.com",
        },
        "button_title": "바로 확인"
    }),
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.json())