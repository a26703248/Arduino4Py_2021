import sqlite3

sql = '''
        CREATE TABLE IF NOT EXISTS STOCK(

          id integer PRIMARY KEY autoincrement,
          證券代號 NVARCHAR(20),
          證券名稱 NVARCHAR(20),
          殖利率 REAL,
          股利年度 INT,
          本益比 REAL,
          股價淨值比 REAL,
          財報年季 NVARCHAR(20),
          ts NVARCHAR(50)
        )
      '''
conn = sqlite3.connect('../case05/twii.db')
curses = conn.cursor()
curses.execute(sql)
conn.commit()
print('完成')
conn.close()