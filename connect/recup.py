import mysql.connector
try:
    connection = mysql.connector.connect(user='root',database='motjeu')
    ben=connection.cursor()
except mysql.connector.Error as e:
    print("=->",e)

def recupMot():
    try:
        b = []
        q=("SELECT * FROM mots")
        ben.execute(q)
        for (id_mot,mot) in ben:
            b.append(mot)
            # print("N°{}: {}\n".format(id_mot,mot))
        return b
    except mysql.connector.Error as e:
        print("=->", e)
    finally:
        #connection.commit()
        ben.close()
        connection.close()
def bestScore():
    try:
        d = []
        q=("SELECT * FROM joueurs ORDER BY score DESC LIMIT 5")
        ben.execute(q)
        for (id_joueur,pseudo,jour,score) in ben:
            d.append(int(score))
            print("{}\t{}\t{}\n".format(pseudo.title(),d,jour))
        # d.sort()
        # d.reverse()
        # print(d)
        #return b
    except mysql.connector.Error as e:
        print("=->", e)
    finally:
        #connection.commit()
        ben.close()