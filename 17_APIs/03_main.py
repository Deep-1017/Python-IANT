# Random Products

import requests

def get_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()
    
    if "data" in data and data["success"] == True:
        print(data["data"]["data"][5]["title"])
    else:
        raise Exception("API request failed or returned an error.")

if __name__ == "__main__":
    get_random_user()