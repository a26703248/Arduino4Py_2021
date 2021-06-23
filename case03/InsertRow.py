import sqlite3

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
sql = 'INSERT INTO Lotto(n1,n2,n3,n4,n5)' \
      'VALUES (1, 3, 5, 7, 9)'

curses.execute(sql)
id = curses.lastrowid # 取得最新的 id
print(id)

conn.commit()
conn.close()
print("完成")