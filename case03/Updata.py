import sqlite3

sql = 'UPDATE Lotto SET n1=%d, n2=%d WHERE id=%d' \
      %(39, 38, 1)
print(sql)

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
curses.execute(sql)

print('Update ok, rowcount:', curses.rowcount)

conn.commit()
conn.close()