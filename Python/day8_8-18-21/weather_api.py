import requests

city_id = 5128581
BASE_URL = "https://api.openweathermap.org/"
route = f"data/2.5/weather?id={city_id}&appid="
api_key = ""


api_request = requests.get(BASE_URL + route + api_key)
response = api_request.json()

if api_request.status_code == 200:
    # print(api_request.json())
    # print(f"Your fact is {api_request.json()['fact']}")
    # print(f"Your fact is {response['fact']}")
    print(f"Your fact is {response}")
    weather = response.get("weather")
    exact_weather = weather[0]
    print(exact_weather.get("main"))

    print(response.get("weather")[0].get("main"))
