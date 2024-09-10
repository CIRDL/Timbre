import requests

url = "https://discoveryprovider.audius.co/v1/users/handle/masego/tracks"

payload = {}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
