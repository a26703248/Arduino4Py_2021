# 絕對溫度 273.15
import requests
import json
import urllib.request
import ssl
# ssl不用驗證

def openWeather():
    city = 'taoyuan'
    count = 'tw'
    apikey = '9843047d16e20413cf8f4203c24e5d29'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}' \
        .format(city, count, apikey)

    resp =requests.get(url)
    status_code = resp.status_code
    if(status_code == 200):
        jo = json.loads(resp.text)
        print(jo)
        main = jo['weather'][0]['main']
        icon = jo['weather'][0]['icon']
        temp = jo['main']['temp']
        feels_like = jo['main']['feels_like']
        humidity = jo['main']['humidity']
        print(main, icon, temp, feels_like, humidity)
        return status_code, main, icon, temp, feels_like, humidity
    else:
        print('ERROR', resp.status_code)
        return status_code, None, None, None, None, None,

def openWeatherIcon(icon):
    img_url = 'https://openweathermap.org/img/wn/%s@2x.png' % icon
    raw_data = urllib.request.urlopen(img_url).read()
    return raw_data


if __name__ == "__main__":
    weather = openWeather()
    print(weather)