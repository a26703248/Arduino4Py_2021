import json
import sqlite3
import threading
import time
import requests

conn = sqlite3.connect('../Project_Demo/weather.db', check_same_thread=False)
curses = conn.cursor()
city = 'taoyuan'
count = 'tw'
apikey = '9843047d16e20413cf8f4203c24e5d29'
# 絕對溫度 273.15

def openWeather():
    # {'coord': {'lon': 121.3187, 'lat': 24.9896}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations',
    # 'main': {'temp': 298.97, 'feels_like': 300.01, 'temp_min': 298.42, 'temp_max': 300.58, 'pressure': 1007, 'humidity': 92}, 'visibility': 10000,
    # 'wind': {'speed': 0.45, 'deg': 25, 'gust': 0.89},
    # 'clouds': {'all': 75}, 'dt': 1624621642,
    # 'sys': {'type': 2, 'id': 2020618, 'country': 'TW', 'sunrise': 1624568797, 'sunset': 1624618071},
    # 'timezone': 28800, 'id': 1667905, 'name': 'Taoyuan District', 'cod': 200}

    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}' \
        .format(city, count, apikey)

    resp = requests.get(url)
    status_code = resp.status_code
    if (status_code == 200):
        jo = json.loads(resp.text)
        # print(jo)
        temp = jo['main']['temp']
        temp = round(((float(temp)) - 273.15), 2)
        maxTemp = jo['main']['temp_max']
        maxTemp = round(((float(maxTemp)) - 273.15), 2)
        minTemp = jo['main']['temp_min']
        minTemp = round(((float(minTemp)) - 273.15), 2)
        feelslikeTemp = jo['main']['feels_like']
        feelslikeTemp = round(((float(feelslikeTemp)) - 273.15), 2)
        humidity = jo['main']['humidity']
        wendspeed = jo['wind']['speed']
        wenddeg = jo['wind']['deg']
        clouds = jo['clouds']['all']
        main = jo['weather'][0]['main']
        country = count
        citys = city
        origin = 'openweather.Web'
        return temp,maxTemp,minTemp,feelslikeTemp,humidity,wendspeed,wenddeg,clouds,main,country,citys,origin
    else:
        print('ERROR', resp.status_code)
        return None,None,None,None,None,None,None,None,None,None,None,None
def InsertDB(list):
    sql = '''
                insert into openweather(temp,maxTemp,minTemp,feelslikeTemp,humidity,wendspeed,wenddeg,clouds,main,country,city,origin)
                Values(?,?,?,?,?,?,?,?,?,?,?,?)
              '''
    curses.execute(sql, list)
    conn.commit()

    print('完成')
    conn.close()
if __name__ == '__main__':
    list = openWeather()
    InsertDB(list)
