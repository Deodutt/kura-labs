## Simple cat fact API with For loop#
# import requests

# BASE_URL = "https://catfact.ninja/"
# route = "fact/"

# api_request = requests.get(BASE_URL + route)
# # response = api_request.json()

# if api_request.status_code == 200:

#     for x in range(10):
#         api_request = requests.get(BASE_URL + route)
#         response = api_request.json()
#         print(f"Your fact {x+1} is {response.get('fact')}")


# using the query.
import requests

BASE_URL = "https://catfact.ninja/"
route = "facts/"
limit = "?limit=10"
api_request = requests.get(BASE_URL + route + limit)
response = api_request.json()

if api_request.status_code == 200:
    # print(response.get("data"))
    print(response.get("data")[0].get("fact"))

    for x in range(len(response.get("data"))):
        print(f"{x + 1}. {response.get('data')[x].get('fact')}")