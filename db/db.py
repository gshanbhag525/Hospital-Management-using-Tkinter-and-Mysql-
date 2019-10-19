import mysql.connector
import sys
global con
con = mysql.connector.connect(
    host = "localhost",
    user = "gunesh",
    password = "gunesh",
    database = "test",
    port = "8889"
)
global cursor
cursor = con.cursor()

def user_login(tup):
    try:
        cursor.execute("SELECT * from `admin` WHERE `username`=%s AND `password`=%s",tup)
        return (cursor.fetchone())
    except:
        return False

def pat_insert(tup):
    try:
        # cursor.execute("INSERT INTO `patient` values", tup)     #VALUES(?,?,?,?,?,?,?,?)
        # cursor.execute("INSERT INTO CONTACT_NO VALUES (?,?,?)', (pp1, pp6, pp7,))

        cursor.execute("insert into patient(pat_id,pat_name,gender,address,contact_no,doc_id) values(%s,%s,%s,%s,%s,%s)", tup)

        con.commit()
        # cursor.close()
        # con.close()
        return True
    except:
        print(sys.exc_info())
        return False

def show_drug_records():
    cursor.execute("select * from drug")
    #fetch all fetch all the data
    return cursor.fetchall()

def show_pat_records():
    cursor.execute("select * from patient")
    return  cursor.fetchall()
