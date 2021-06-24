
'''
 本益比: 還本年限 <= 10
 值利率: > 7%
 股價淨值比: 小於 1 合適買進, 大於 1 適合賣出
'''
import sqlite3

bs = float(input('買進(1)賣出(2)查看股票(3)'))
if bs == 3:
    symbol = input('請輸入股票代號:')
    sql ='''
            select 證券代號,證券名稱,本益比,殖利率,股價淨值比, ts from STOCK
            where 證券代號 = '%s'
         ''' % (symbol)
else:
    pe = float(input('請輸入本益比:'))
    r = float(input('請輸入值利率:'))
    # "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
    sql = '''
            select 證券代號,證券名稱,本益比,殖利率,股價淨值比, ts from STOCK
            where (本益比 <= %f and 本益比 > 0) and 
                  (殖利率 >= %f and 殖利率 > 0) and
                  (股價淨值比 %s 1 and 股價淨值比 > 0)
          ''' % (pe, r, '<' if bs == 1 else '>=')

conn = sqlite3.connect('twii.db')
curses = conn.cursor()
curses.execute(sql)
result = curses.fetchall()

for r in result:
    print(r)

conn.close()