import pymysql
from util.DB import DB


class dbConnect:
    def createUser(uid, name, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (uid, name, email, password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email = %s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print (e + 'が発生してます')
            abort(500)
        finally:
            cur.close()

    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生してます')
            abort(500)
        finally:
            cur.close()

    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id =%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name = %s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def addChannel(uid, newChannelName, NewChannelDeccriotion):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, name,abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDeccriotion))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def deleteChannel(cid):
        try:
            conn = DB.connection()
            cur = conn.cursor()
            sql = "DELETE FROM channel WHERE id = %s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id,u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()

            return messages
        except Exception as e:
            print (e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close()

    def DeleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id = '%s';"
            cur.execute(sql, (message_id,))
            conn. commit()
        except Exception as e:
            print (e + 'が発生しています')
            abort(500)
        finally:
            cur.close()
