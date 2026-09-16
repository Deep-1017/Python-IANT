import requests

def get_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data = response.json()
    print(data["data"]["data"][5]["location"]["city"])
    
get_random_user()