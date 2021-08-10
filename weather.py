import requests


url = "https://wttr.in/san%20francisco"
payload = {"nTqu": "", "lang": "en"}

response = requests.get(url, params=payload)
response.raise_for_status()

print(response.text)
