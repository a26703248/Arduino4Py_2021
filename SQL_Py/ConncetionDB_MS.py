import pymssql


conn = pymssql.connect(server='MSI.database.windows.net', user='Supplied', password='1234', database='Java')
cursor = conn.cursor()
sql = '''
        SELECT * FROM TEST
      '''

cursor.execute(sql)
row = cursor.fetchone
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()