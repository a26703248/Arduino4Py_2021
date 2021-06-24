import sqlite3
import requests

path = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210623&selectType=ALL'

csv = requests.get(path).text

# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",

for r in range(1, 9):
    s = '"{},'.format(r)
    e = '"{}'.format(r)
    csv = csv.replace(s, e)
csv = csv.replace('"', '')
csv = csv.replace('-', '-1')
rows = csv.split('\r\n')

stocks = []
for r in rows:
    list = r.split(',')
    if len(list) == 8 and list[0] != '證券代號':
        #print(list)
        list[2] = float(list[2]) # 殖利率(%)
        list[3] = int(list[3]) # 股利年度
        list[4] = float(list[4])  # 本益比
        list[5] = float(list[5])  # 股價淨值比
        list[5] = float(list[5])  # 股價淨值比
        list[7] = '2021-06-23'  # 股價淨值比
        stocks.append(tuple(list))

print(stocks)

# 匯入資料庫
sql = '''
        insert into Stock (證券代號,證券名稱,殖利率,股利年度,本益比,股價淨值比,財報年季,ts)
        values(?,?,?,?,?,?,?,?)
      '''
conn = sqlite3.connect('twii.db')
curses = conn.cursor()
curses.executemany(sql, stocks)
conn.commit()

conn.close()