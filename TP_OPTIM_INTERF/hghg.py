import pandas as pd
from os import listdir
import sys
import re
import timeit
import csv


pathh= 'C:/Users/Abdelbari/Documents/test_moy'


def next_fit( weights, C):
    curr_bin = {'available_capacity': C, 'items': []}
    conf = {'n_bins': 1, 'bins': [curr_bin]}
    start_time = timeit.default_timer()
    for w in weights:
        if w < curr_bin['available_capacity']:
            # insert_last_bin()
            curr_bin['items'].append(w)
            # update_conf()
            curr_bin['available_capacity'] -= w
        elif w <= C:
            # insert_last_bin()
            curr_bin = {'available_capacity': C - w, 'items': [w]}
            conf['bins'].append(curr_bin)
            # update_conf()
            conf['n_bins'] += 1
        else:
            print(w, C)
            return 0, None
        time = timeit.default_timer() - start_time
    return conf['n_bins'], conf, time

def InstanceReader(filepath):
    try:
        # filepath = input("Saisir le nom du fichier: ")
        # filepath = "./data1/N1C1W1_A.txt"
        reader = open(filepath, mode='r')
    except FileNotFoundError:
        print("Le fichier d'instance fourni n'existe pas")
        exit()

    if sys.platform == 'windows':
        lst = filepath.split("\\")
    else:
        lst = filepath.split("/")

    instance = lst[-1].split(".")[0]  # Recuperer nom de l'instance
    n = int(reader.readline())
    c = int(reader.readline())
    w = []
    for i in range(n):
        w.append(int(reader.readline()))
    reader.close()
    return (instance, n, c, w)

def InstanceReader2(l):
    try:
        with open('s_optim.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[-1]==l:
                    h = row[1]

    except FileNotFoundError:
        print("Le fichier d'instance fourni n'existe pas")
        exit()
    return h


files = listdir(pathh)

print(files)
print(len(files))
open("resultat_test.csv", "w").close()
for f in files:
    l = pathh + "/"+f
    print(l)
    j = InstanceReader2(f)
   # print("hada",j)
    instance,n,C,w = InstanceReader(l)


    nb, conf, time = next_fit(w,C)

    resultat = open("resultat_test.csv", mode="a+")

    resultat.write(f'{instance},{n},{C},{nb},{j},{time*1000}\n')  # Ecrire les resultats dans un fichier csv
    resultat.close()
   # InstanceReader2()
