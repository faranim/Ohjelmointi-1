import requests

api_key = "API_AVAIN" # Syötä oma API-avain tähän
city = input("Anna paikkakunnan nimi: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15
    print(f"Sää paikkakunnalla {city} on {description} ja lämpötila on {temperature_celsius:.1f} astetta Celsius-asteina.")
else:
    print("Virhe haettaessa säätietoja")
