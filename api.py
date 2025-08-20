import requests


def get_data():
    url = "https://api.github.com"
    response = requests.get(url)
    return response.json()


print(get_data())
