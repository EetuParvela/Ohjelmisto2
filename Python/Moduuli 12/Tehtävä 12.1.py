import requests

request = "https://api.chucknorris.io/jokes/random"
answer = requests.get(request).json()

print(answer["value"])