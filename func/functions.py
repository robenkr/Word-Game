#-*-coding:utf-8 *-
#!/usr/bin/env python

try:
    import sys
    import os
    from random import shuffle, choice
    from connect.recup import *
    from connect.insertdb import insertJoeurs
    from string import *
    from time import *
    import datetime
except NameError:
    print("Error accessing folders")
except TypeError as e:
    print("=-> ",e)

jour = datetime.date.today()
words = "../connect/frenchssaccent.dic"

class Jeux:
    """
        Class containing the driving idea of the game!
         And return 2 values: the points obtained & the choice of resumption of the game ...
    """

    def __init__(self):
        self.mot = ""
        self.point = 0

    def choixMot(self, mots):
        """
        Method for making the random choice of a word in the list retrieved
        :param mots:
        :return: mot
        """
        self.mot = choice(mots)
        if len(self.mot) < 2:
            self.mot = choice(mots)
        # print(">>>" + self.mot)
        return self.mot

    def melerMot(self, m):
        """
        Method that takes a word and returns the mixed
        :param m:
        :return:
        """
        self.t = len(m)
        self.l = [i for i in range(self.t)]
        shuffle(self.l)
        self.n = ''
        for x in self.l:
            self.n += m[x]
        # print(self.n)
        return self.n.upper()

    def verifierReponse(self, reponse, mystere):
        """
        Method to verify the validity of the response
        :param reponse:
        :param mystere:
        :return:
        """
        if (reponse.upper()) != mystere.upper():
            print("\nDésolé vous avez échoué! le bon mot était : " + mystere.upper())
        else:
            self.point += 2
            print("\nFellicitation vous avez trouvé le mot!\n***" + reponse.upper()+"***")
        choix = input("\nDésirez-vous réprendre?(OUI/NON)>(1/0)")
        return choix, self.point
