import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*'
}

r = requests.post('https://openapiuat.airtel.africa/auth/oauth2/token', headers=headers)

print(r.json())

