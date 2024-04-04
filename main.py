import requests

a = input("Введите широту: ")
b = input("Введите долготу: ")

api = "https://api.open-meteo.com/v1/forecast?latitude=" + a + "&longitude=" + b + "&current=temperature_2m,wind_speed_10m"

response = requests.get(api)

if response.status_code == 200:
    response_dict = response.json()
    result_data = response_dict["current"]

    cTime = result_data["time"]
    temperature = result_data["temperature_2m"]
    windSpeed = result_data["wind_speed_10m"]

    print("Время: ", cTime)
    print("Температура: ", temperature, "°C")
    print("Скорость ветра: ", windSpeed, "km/h")
else:
    print(response.status_code)