import sqlite3

sql = 'DELETE FROM Lotto WHERE id=%d' % (1)
print(sql)

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
curses.execute(sql)

print('Update ok, rowcount:', curses.rowcount)

conn.commit()
conn.close()