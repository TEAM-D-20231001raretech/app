import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="petalk-db.c7k0ajlbmrfb.ap-northeast-1.rds.amazonaws.com",
            db="petalkDB",
            user="admin",
            password="petalkPasswd",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
