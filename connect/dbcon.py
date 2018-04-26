import mysql.connector
from mysql.connector import errorcode

try:
    config = {'host':'localhost',
              'user':"root",
              'password':'',
              'database':'motjeu',
            'raise_on_warnings': True
            }
    connection = mysql.connector.connect(**config)

    ben = connection.cursor()
    ben.execute("CREATE TABLE IF NOT EXISTS mots("
                " id_mot INT(11) PRIMARY KEY AUTO_INCREMENT,"
                " mot VARCHAR(255) NOT NULL"
                ")")
    ben.execute("CREATE TABLE IF NOT EXISTS joueurs("
                " id_joueur INT(11) PRIMARY KEY AUTO_INCREMENT,"
                " pseudo VARCHAR(255) NOT NULL,"
                "jour date NOT NULL,"
                "score VARCHAR (255) NOT NULL"
                ")")

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error with password or username-> ",e)
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("this Database does not exist-> ", e)
    else:
        print("=->",e)
else:
    connection.close()

#==========================================for SQLITE3===============================
# import sqlite3
# from Mot_Jeux.MotJeux2.func.functions import *
# try:
#     connect = sqlite3.connect('motJeu.db')
#
#     ben =connect.cursor()
#     # ben.execute("""
#     # CREATE TABLE IF NOT EXISTS mots(id_mot INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, mot TEXT)
#     # """)
#     connect.commit()
#
#     b = suppEspace(recup())
#     #print(b)
#     #print(b[50])
#     k='r'
#     data = {"mot": "olivier"}
#     ben.execute("""INSERT INTO mots(mot) VALUES(:mot)""",data)
#
#
#     # for i in b :
#     #     ben.executemany("""
#     #     INSERT INTO mots(mot) VALUES(?);""",i)
#
# # except sqlite3.OperationalError:
# #     print("La table existe deja"e:)
# except Exception as e:
#     print("Erreur-> ",e)
#     connect.rollback()
# finally:
#     connect.close()
