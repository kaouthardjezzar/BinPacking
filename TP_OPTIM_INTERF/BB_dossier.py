# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifier_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import timeit

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog

import csv
import bin
import pandas as pd
from os import listdir
import re

# global variables
files_regex = 'N([0-9]+)C([0-9]+)W([0-9]+)_([A-T]).txt'
pathh = ''


class Ui_BB_dossier(QWidget):

    def loadData_mod_csv(self, fileName):

        with open(fileName, "rb") as users:

            for row_number, user in enumerate(users):

                # print(row_number)
                # print(user)
                t = str(user)
                t1 = t[2:-12]
                jk = t1.split(",")
                # print(t)
                # print(t1)
                # print(jk)

                self.tableWidget_anc.insertRow(row_number)

                for column_number in range(len(jk)):
                    # print(column_number)
                    # print(data)
                    self.cell = QtWidgets.QTableWidgetItem(jk[column_number])
                    self.tableWidget_anc.setItem(row_number, column_number, self.cell)

    def openFileNameDialog(self):
        global pathh
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        print(file)
        pathh = file

    def InstanceReader(self, filepath):
        try:
            # filepath = input("Saisir le nom du fichier: ")
            # filepath = "./data1/N1C1W1_A.txt"
            reader = open(filepath, mode='r')
        except FileNotFoundError:
            print("Le fichier d'instance fourni n'existe pas")
            exit()

        lst = filepath.split("/")

        instance = lst[-1].split(".")[0]  # Recuperer nom de l'instance
        n = int(reader.readline())
        c = int(reader.readline())
        w = []
        for i in range(n):
            w.append(int(reader.readline()))
        reader.close()
        return (instance, n, c, w)

    def InstanceReader2(self, l):

        try:

            with open('s_optim.csv', newline='') as f1:

                reader = csv.reader(f1)
                for row in reader:
                    if row[-1] == l:
                        h = row[1]

        except FileNotFoundError:
            print("Le fichier d'instance fourni n'existe pas")
            exit()
        return h

    def branchAndBound(self, c, w):
        n = len(w)
        print(n, n)
        minBoxes = n  # initialiser la valeur optimale à n
        Nodes = []  # les noeuds à traiter
        wRemaining = [c] * n  # initialiser les poids restants dans chaque boite [c,c,c,.......c]
        numBoxes = 0  # initialiser le nombre de boites utilisées
        for k in range(len(w)):
            if w[k] > c:
                print("les poids des objets ne doivent pas dépasser la capacité du bin")
                return 0
            else:
                print(n, n)
                curN = bin.Node(wRemaining, 0,
                                numBoxes)  # créer le premier noeud, niveau 0, nombre de boites utilisées 0

                Nodes.append(curN)  # ajouter le noeud à l'arbre

                while len(Nodes) > 0:  # tant qu'on a un noeud à traiter

                    curN = Nodes.pop()  # récupérrer un noeud pour le traiter (curN)
                    curLevel = curN.getLevel()  # récupérrer son niveau

                    if (curLevel == n) and (
                            curN.getNumberBoxes() < minBoxes):  # si c'est une feuille et nbr boites utilisées < minBoxes
                        minBoxes = curN.getNumberBoxes()  # umettre à jour minBoxes

                    else:

                        indNewBox = curN.getNumberBoxes()

                        if (indNewBox < minBoxes):

                            wCurLevel = w[curLevel]
                            for i in range(indNewBox + 1):
                                if (curLevel < n) and (curN.getWRemaining(
                                        i) >= wCurLevel):  # si cet possible d'insérer l'objet dans la boite i
                                    # on crée un nouveau noeud.
                                    newWRemaining = curN.getWRemainings().copy()
                                    newWRemaining[i] -= wCurLevel  # la capacité restante i - le poids du nouvel objet

                                    if (i == indNewBox):  # nouvelle boite
                                        newNode = bin.Node(newWRemaining, curLevel + 1, indNewBox + 1)
                                        for j in range(curLevel + 1, len(w)):
                                            s = + w[j]
                                        if (((indNewBox + 1) + s / c) < minBoxes):
                                            Nodes.append(newNode)
                                    else:  # boite deja ouverte
                                        newNode = bin.Node(newWRemaining, curLevel + 1, indNewBox)
                                        for j in range(curLevel + 1, len(w)):
                                            s = + w[j]
                                        if ((indNewBox + s / c) < minBoxes):
                                            Nodes.append(newNode)

                return minBoxes

    def execDir(self):
        global pathh
        pat = pathh
        print(type(pathh))
        files = listdir(pathh)
        open("result_bb.csv", "w").close()
        print(1)
        print(pat)
        for f in files:
            l = pat + "/" + f
            print(f)
            j = self.InstanceReader2(f)
            print("hada", j)
            instance, n, C, w = self.InstanceReader(l)

            start = timeit.default_timer()
            c = self.branchAndBound(C, w)
            stop = timeit.default_timer()
            time = stop - start
            resultatt = open("result_bb.csv", mode="a+")

            resultatt.write(f'{instance},{n},{C},{c},{j},{time * 1000}\n')  # Ecrire les resultats dans un fichier csv
            resultatt.close()
            print(0)
        self.loadData_mod_csv('./result_bb.csv')

    def setupUi(self, BB_dossier):
        BB_dossier.setObjectName("BB_dossier")
        BB_dossier.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(BB_dossier)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget_anc = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_anc.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_anc.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_anc.setObjectName("tableWidget_anc")
        self.tableWidget_anc.setColumnCount(7)
        self.tableWidget_anc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anc.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.tableWidget_anc, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        BB_dossier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BB_dossier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 18))
        self.menubar.setObjectName("menubar")
        BB_dossier.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BB_dossier)
        self.statusbar.setObjectName("statusbar")
        BB_dossier.setStatusBar(self.statusbar)

        self.retranslateUi(BB_dossier)
        QtCore.QMetaObject.connectSlotsByName(BB_dossier)

        self.pushButton.clicked.connect(self.execDir)
        self.pushButton_2.clicked.connect(self.openFileNameDialog)

    def retranslateUi(self, BB_dossier):
        _translate = QtCore.QCoreApplication.translate
        BB_dossier.setWindowTitle(_translate("BB_dossier", "MainWindow"))
        self.label.setText(_translate("BB_dossier", "Selectionner le dossier de test"))
        self.pushButton_2.setText(_translate("BB_dossier", "Selectionner"))
        self.pushButton.setText(_translate("BB_dossier", "Tester"))
        item = self.tableWidget_anc.horizontalHeaderItem(0)
        item.setText(_translate("imp_rdv", "File"))
        item = self.tableWidget_anc.horizontalHeaderItem(1)
        item.setText(_translate("imp_rdv", "Capacity"))
        item = self.tableWidget_anc.horizontalHeaderItem(2)
        item.setText(_translate("imp_rdv", "items"))
        item = self.tableWidget_anc.horizontalHeaderItem(3)
        item.setText(_translate("imp_rdv", "nbr_bin"))
        item = self.tableWidget_anc.horizontalHeaderItem(4)
        item.setText(_translate("imp_rdv", "Slt_exact"))
        item = self.tableWidget_anc.horizontalHeaderItem(5)
        item.setText(_translate("imp_rdv", "T_exe"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BB_dossier = QtWidgets.QMainWindow()
    ui = Ui_BB_dossier()
    ui.setupUi(BB_dossier)
    BB_dossier.show()
    sys.exit(app.exec_())
