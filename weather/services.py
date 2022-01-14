import urllib.request, urllib.parse, urllib.error
import json
import ssl


fhand = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=california,usa&APPID=25e8b9e17b72a2d527b94198844c9fe2')
data = fhand.read()
file = data.decode()
js = json.loads(file)

def get_weather():
    data = []
    data.append(js['name'])
    data.append(js['weather'][0]['description'])
    data.append(js['main']['temp'])
    data.append(js['main']['temp_max'])
    return data
