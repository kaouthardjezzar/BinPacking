import timeit


class Bin:
    def __init__(self, c):
        self.c = c
        self.r = c
        self.items = []
        self.nb = 0

    def addItem(self, item):
        if self.r >= item:
            self.items.append(item)
            self.nb += 1
            self.r -= item
            return False  # Retourne faux  pour indiquer la fin de l'ajout et l'arret de la boucle
        else:
            return True

    def showItems(self):
        print(self.items)


class FFBinPack:
    def __init__(self, c, w):
        self.c = c  # Capacité du bin
        self.w = sorted(w, reverse=True)  # Trier les elements par ordre decroissant
        self.bins = []  # Creer une liste de bin
        self.bins.append(Bin(c))  # Ajouter un bin a la liste
        self.n = 1  # nombre de bins

    def binpack(self):
        debut = timeit.default_timer()
        for i in self.w:
            add = True
            nb = 0
            while add and nb < self.n:
                add = self.bins[nb].addItem(i)
                nb += 1
            if add:
                bin = Bin(self.c)
                bin.addItem(i)
                self.bins.append(bin)
                self.n += 1
        fin = timeit.default_timer() - debut
        return (fin, self.n)

class Node:
    def __init__(self, wRemaining, level, numBoxes):
        self.wRemaining = wRemaining    #Tableau des poids restants pour chaque boîte
        self.level = level              #Le niveau du noeud dans l'arbre
        self.numBoxes = numBoxes        #nombre de boîtes utilisées

    def getLevel(self):
        return self.level

    def getNumberBoxes(self):
        return self.numBoxes

    def getWRemainings(self):
        return self.wRemaining

    def getWRemaining(self, i):
        return self.wRemaining[i]