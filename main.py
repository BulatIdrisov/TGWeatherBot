#a4ab9918d46fbaf7f59a43958774839d
import requests
import json
def weather(city):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()
        weather_data_structure = json.dumps(weather_data, indent=2)
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        a = 'Сейчас в городе'+' '+city+' '+str(temperature)+' '+'°C, '
        a += 'ощущается как'+' '+ str(temperature_feels)+' '+ '°C'
    except KeyError:
        a = "Такого населённого пункта не существует"
    return a

