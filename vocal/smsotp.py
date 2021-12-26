import requests

url = "https://d7-verify.p.rapidapi.com/send"

payload = "{\r\n    \"expiry\": 900,\r\n    \"message\": \"Your otp code is {code}\",\r\n    \"mobile\": +917047906198,\r\n    \"sender_id\": \"SMSInfo\"\r\n}"
headers = {
    'content-type': "application/json",
    'authorization': "undefined",
    'x-rapidapi-host': "d7-verify.p.rapidapi.com",
    'x-rapidapi-key': "6da8665c0cmshba01ff24fd9a531p103a8ajsnbae824d4dbcf"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)