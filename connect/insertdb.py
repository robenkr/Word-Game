from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(user='root',database='motjeu')
    ben=connection.cursor()
except mysql.connector.Error as e:
    print("=->", e)
def insertMots(b):
    try:
        for i in b:
            moT= ('',i)
            roland = ("INSERT INTO mots"
                    "(id_mot,mot)"
                    "VALUES (%s,%s)")
            ben.execute(roland,moT)
        print('Recording done with Succes!!!')

    except mysql.connector.Error as e:
        print("=->", e)
    finally:
        connection.commit()
        ben.close()
        connection.close()

def insertJoeurs(nom,jour,points):
    if (nom and jour and points) != "":
        try:
            info = ('',nom,jour,points)
            joueur = ("INSERT INTO joueurs"
                      "(id_joueur,pseudo,jour,score)"
                      "VALUES(%s,%s,%s,%s)")
            ben.execute(joueur,info)
        except mysql.connector.Error as e:
            print("=->", e)
        finally:
            connection.commit()
            ben.close()
            connection.close()
    else:
        print("No recordings made!")

