import requests
from PIL import Image

BASE_URL = "https://randomuser.me/"
route = "api/"


api_request = requests.get(BASE_URL + route)
response = api_request.json()

if api_request.status_code == 200:

    person = response.get("results")[0]
    # print(person)

    print(
        f"{person.get('name').get('first')} {person.get('name').get('last')} is from {person.get('location').get('country')}"
    )
    if person.get("gender") == "female":
        verb = "she"
    else:
        verb = "he"

    print(f"{verb.title()} is {person.get('dob').get('age')} years old.")

    # Printing the image of the random user
    random_user_image = person.get("picture").get("large")
Image.open(requests.get(random_user_image, stream=True).raw)
