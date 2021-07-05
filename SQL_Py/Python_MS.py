import pymssql
conn = pymssql.connect(host='192.168.0.10',
                       user='supplied',
                       password='1234',
                       database='java')
cursor = conn.cursor()
cursor.execute("select * from empolyee")
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()