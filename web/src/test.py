import requests
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '7ba50bb3cf2136baafa3e8a344926bc3'
redirect_uri = 'https://example.com/oauth'
authorize_code = '-fnLY4sVuj5zwFa11RCena1sf9UlTI3SOFGf-h-eGiYcTkNEI1fB7Bl6NWRKic46-lGQLAorDR4AAAGJZ985RA'
client_secret = '0bbVT54CBT7J66HkbjZ4m1QiGONyocz8'
data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    'client_secret': client_secret
    }
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)
# json 저장
import json
with open(r"C:\Users\Playdata\Desktop\kakao_code.json","w") as fp:
    json.dump(tokens, fp)