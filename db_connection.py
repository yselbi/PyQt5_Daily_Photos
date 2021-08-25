###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
#  File name: db_connection
#
################################################################


import mysql.connector as mysql


def connect_db(user="", query="", rw="", username="", pw="", tuple_data=()):
    try:
        if user == "admin":
            """ to be able to connect to MySQL DMS use admin name as root and password as 123456 or set credentials below
                as you set your own """
            con = mysql.connect(host="localhost", user="root", password="123456", database="daily_photos")
            cur = con.cursor()
            cur.execute(query)
            if rw == "r":
                data = cur.fetchone()
                return data
            else:
                con.commit()
                return True

        else:
            con = mysql.connect(host="localhost", user=username, password=pw, database="daily_photos")
            cur = con.cursor()
            if rw == "r":
                cur.execute(query)
                data = cur.fetchall()
                return (data, True)
            else:
                cur.execute(query, tuple_data)
                con.commit()
                return True
    except mysql.Error as err :
        return str(err)

    finally:
        con.close()

