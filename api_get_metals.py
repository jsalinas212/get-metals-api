import requests
import json

access_key = "[Access Key Here]"

url = f'https://metals-api.com/api/latest?access_key={access_key}&symbols=xau,xag'

response = requests.get(url)
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)

print(dictionary)