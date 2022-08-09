import requests
import json



data = {"email": "gritzman@mindspring.com", "password": "Tamara12"}

s = requests.Session()

r = s.post('https://app.universaltennis.com/api/v1/auth/login',json=data)


# print(r.status_code)
# print(r.headers)
# cookies = r.cookies

query = {"query": "Yair Gritzman"}
utr = s.get('https://api.universaltennis.com/v2/search', data=query)

# utr = requests.get('https://app.universaltennis.com/search?query=Yair&type=players&utrFitPosition=6&utrMax=16&utrMin=1&utrTeamType=singles&utrType=verified')

utr = utr.json()
print(utr["players"]["hits"][0]["source"]["singlesUtr"])