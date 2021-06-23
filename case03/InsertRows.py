import random
import sqlite3

conn = sqlite3.connect('demo.db')
curses = conn.cursor()
lottos = [] # 建立一組陣列(List {})可改動的陣列,資料分析時會比較快速

for i in range(999):
    #取出 1~39 的不重複數字 5 個
    nums = set()
    while len(nums) < 5:
        n = random.randint(1, 39)
        nums.add(n)
    lottos.append(tuple(nums)) # 要轉成元組陣列 () 不可改動的陣列,資料分析時會比較快速

print(lottos)

sql = 'INSERT INTO Lotto(n1,n2,n3,n4,n5)' \
      'VALUES (?, ?, ?, ?, ?)'
curses.executemany(sql, lottos)

conn.commit()
conn.close()
print("完成")