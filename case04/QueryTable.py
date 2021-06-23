#請寫出最高薪的人名
import sqlite3

sql = '''
        SELECT 'MAX' AS TYPE, name, max(salary) as SALARY FROM Employee
        UNION ALL
        SELECT 'MIN' AS TYPE, name, min(salary) as SALARY FROM Employee
      '''

conn = sqlite3.connect('../case03/demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)

conn.commit()
conn.close()
