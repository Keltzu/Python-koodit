import requests

api_key = "602070207811e1ffd0cb778f0f665d4a"
city = "Helsinki"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Sää Helsingissä: {weather}, Lämpötila: {temperature} °C")
else:
    print("Paikkakuntaa ei löytynyt.")