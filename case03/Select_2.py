import sqlite3
# 查出 n1+ ... + n5 = 40
#有哪些?

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
sql = 'SELECT n1, n2, n3, n4, n5 FROM Lotto '
curses.execute(sql)
rows = curses.fetchall()

d = {}
for r in range(1,40):
    d[r] = 0
print(d)

for r in rows:
    for i in range(1,5):
        d[r[i]] = d[r[i]] + 1

print(d)
maxValue = max(d.values())
minValue = min(d.values())
print(maxValue)
print(minValue)

for k, v in d.items():
    if v == maxValue:
        print("%d(%d)" % (k, maxValue))
    if v == minValue:
        print("%d(%d)" % (k, minValue))

curses.close()