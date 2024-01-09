import requests

response = requests.get('https://randomuser.me/api')

# check if app connected, 200 if connected
print(response.status_code)

print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)