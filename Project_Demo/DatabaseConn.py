import sqlite3

# {'coord': {'lon': 121.3187, 'lat': 24.9896}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 301.25, 'feels_like': 306.5, 'temp_min': 299.28, 'temp_max': 302.66, 'pressure': 1008, 'humidity': 86}, 'visibility': 10000, 'wind': {'speed': 2.06, 'deg': 310}, 'clouds': {'all': 75}, 'dt': 1624589706, 'sys': {'type': 2, 'id': 2020618, 'country': 'TW', 'sunrise': 1624568797, 'sunset': 1624618071}, 'timezone': 28800, 'id': 1667905, 'name': 'Taoyuan District', 'cod': 200}

sql = '''
        create table if not exists WEATHER(
            id integer primary key autoincrement,
            temp float not null,
            maxTemp float not null,
            minTemp float not null,
            feelslikeTemp float not null,
            humidity float not null,
            wendspeed float not null,
            wenddeg float not null,
            clouds int not null,
            main NVARCHAR(20),
            country NVARCHAR(20) not null,
            city NVARCHAR(20) not null,
            ts NVARCHAR(50) not null
        )
      '''

conn = sqlite3.connect('weather.db')
curses = conn.cursor()
curses.execute(sql)

conn.commit()
print('完成')

conn.close()