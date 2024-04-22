#!/bin/python3
import requests

longitude=3.06
latitude=50.63

icons = {
         "clear sky":"☀️ ",
         "few clouds":"🌤️ ",
         "scattered clouds":"⛅ ",
         "broken clouds":"🌥️ ",
         "overcast clouds":"☁️ ",
         "light rain":"🌦️ ",
         "moderate rain":"🌧️ ",
         "heavy intensity rain":"🌧️ ",
         "very heavy rain":"🌧️ ",
         "extreme rain":"🌧️ ",
         "freezing rain":"🌨️ ",
         "light intensity shower rain":"🌧️ ",
         "shower rain":"🌧️ ",
         "heavy intensity shower rain":"🌧️ ",
         "ragged shower rain":"🌧️ ",
         "thunderstorm with light rain":"⛈️ ",
         "thunderstorm with rain":"⛈️ ",
         "thunderstorm with heavy rain":"⛈️ ",
         "light thunderstorm":"🌩️ ",
         "thunderstorm":"🌩️ ",
         "heavy thunderstorm":"🌩️ ",
         "ragged thunderstorm":"🌩️ ",
         "thunderstorm with light drizzle":"⛈️ ",
         "thunderstorm with drizzle":"⛈️ ",
         "thunderstorm with heavy drizzle":"⛈️ ",
         "light snow":"🌨️ ",
         "snow":"❄️ ",
         "heavy snow":"❄️ ",
         "sleet":"☃️ ",
         "shower sleet":"☃️ ",
         "light rain and snow":"🌨️ ",
         "rain and snow":"🌨️ ",
         "light shower snow":"🌨️ ",
         "shower snow":"🌨️ ",
         "heavy shower snow":"🌨️ ",
         "mist":"🌫️ ",
         "smoke":"🌫️ ",
         "haze":"🌫️ ",
         "fog":"🌫️ ",
         "sand":"🌫️ ",
         "dust":"🌫️ ",
         "light intensity drizzle":"🌫️ ",
         "volcanic ash":"🌋 ",
         "tornado":"🌪️ "
}


def get_weather_forecast(longitude, latitude):
    # I'm living in a country that uses a unit system that makes sense.
    params = {"units": "metric",
              "appid": "2b5e29560749e7244342efc00227bae0",
              "lat": latitude, "lon": longitude}
    resp = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params=params)
    if not resp.ok:
        raise IOError(resp.text)
    return resp.json()
    
try:
    action = '~/.config/sway/scripts/sway-sensible-terminal --title "__weather__" -o window.dimensions.columns=74 window.dimensions.lines=46 -e bash -c "curl v2.wttr.in/'+str(latitude)+','+str(longitude)+' ;read"'
    weather = get_weather_forecast(longitude,latitude)
    ico = icons.get(weather.get("weather")[0].get("description"))
    if not ico:
        ico = weather.get("weather")[0].get("description")
    temp = weather.get("main").get("temp")
    if temp == None:
        temp = "NaN"
    print("weather|string|"+ico)
    print("temp|float|"+str(temp))
    print("action|string|"+action)
    print()
except:
    print("weather|string| ")
    print("temp|float|")
    print("action|string|")
    print()
