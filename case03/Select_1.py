import sqlite3

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
# 查詢資料列 META-INFO
curses.execute('PRAGMA TABLE_INFO("Lotto")')
#print(curses.fetchall())
names = [ t[1] for t in curses.fetchall()]

for n in names:
    print(n, end='\t')
print('\n----------------------------------------------------------')
# 查詢資料列 sql
sql = 'SELECT id, n1, n2, n3, n4, n5, ts FROM Lotto'
curses.execute(sql)
rows = curses.fetchall()

for r in rows:
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'
          .format(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
