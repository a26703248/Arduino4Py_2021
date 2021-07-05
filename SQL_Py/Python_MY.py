import pymysql as pymysql

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "a0909007892",
    "db": "java",
    "charset": "utf8"
}
sql = '''
        SELECT * FROM empolyee
      '''
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 執行指令
        cursor.execute(sql)
        # 取得第一筆資料
        result = cursor.fetchall()
        print(result)
except Exception as ex:
    print('失敗')