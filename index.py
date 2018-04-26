#-*-coding:utf-8 *-
#!/usr/bin/env python

try:
    from func.functions import *
except NameError:
    print("Error accessing folders")
except TypeError:
    print("Packages Access Error")

#============================================================================
b = recupMot()
monJeux = Jeux()

choix = -1
point = 0
while choix != str(0):
    r = monJeux.choixMot(b)
    s = monJeux.melerMot(r)
    print("\t"+s.upper())

    reponse = str(input("Please enter the correct word: "))
    resultat = monJeux.verifierReponse(reponse, r)

    choix = resultat[0]

point = resultat[1]
print("Final score: ", point)
pseudo = str(input("Enter your name: "))
try:
    insertJoeurs(pseudo,jour,point)
except Exception as e:
    print("===>{}".format(e))

#============================================================================
