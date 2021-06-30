import sqlite3

sql = '''
        CREATE TABLE if not exists LocalWeather(
            id integer primary key autoincrement,
            cds real,
            temp real,
            humi real,
            ts timestamp default current_timestamp
        )
      '''
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()


