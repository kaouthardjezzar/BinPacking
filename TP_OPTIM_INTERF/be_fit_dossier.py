# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifier_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import timeit

from item import Item
from random import shuffle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog

import csv
import pandas as pd
from os import listdir
import re
from binbin import Bin
import bin

#global variables
files_regex='N([0-9]+)C([0-9]+)W([0-9]+)_([A-T]).txt'
pathh = ''


class Heuristic:
    @staticmethod
    def apply(item, bins):
        """
        Applies the heuristic to the given bins. This has to be overridden by subclasses.
        :param item: The item to add.
        :param bins: The list of bins to choose from.
        :return: The lists of bins after insertion.
        """
        return bins


class BestFit(Heuristic):
    @staticmethod
    def apply(item, bins):
        """
        Adds the item to the bin for which the least amount of open space would be available after insertion.
        :param item: The item to add.
        :param bins: The bins to choose from.
        :return: The list of bins after the insertion.
        """
        valid_bins = (b for b in bins if b.can_add_item(item))
        # Note that this method is exactly the same as for the BestFit heuristic except for the following line.
        sorted_bins = sorted(valid_bins, key=lambda x: x.filled_space(), reverse=True)
        if sorted_bins:
            b = sorted_bins[0]
        else:
            b = Bin(bins[0].capacity)
            bins.append(b)
        b.add_item(item)
        return bins


class Loadingg(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)
        self.setWindowFlag(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.movie = QMovie('111.gif')
        self.label_anim = QLabel(self)
        self.label_anim.setMovie(self.movie)
        self.start_anim()

        self.show()

    def start_anim(self):
        self.movie.start()

    def stop_anim(self):
        self.movie.stop()
        self.close()

class Ui_be_fit_dossier(QWidget):


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

    def execDir(self):
        global pathh
        pat = pathh
        files = listdir(pathh)
        open("result_b.csv", "w").close()
        print(1)
        print(pat)
        for f in files:
            l = pat + "/" + f
            print(f)
            j = self.InstanceReader2(f)
            print("hada", j)
            instance, n, C, w = self.InstanceReader(l)
            items = [Item(size=int(i)) for i in w]
            shuffle(items)
            start = timeit.default_timer()
            bins = [Bin(capacity=C)]
            for item in items:

                bins = BestFit.apply(item, bins)
            stop = timeit.default_timer()
            time = stop - start
            c = len(bins)
            print("aham")
            resultatt = open("result_b.csv", mode="a+")

            resultatt.write(f'{instance},{n},{C},{c},{j},{time * 1000}\n')  # Ecrire les resultats dans un fichier csv
            resultatt.close()
        print(pathh)
        self.loadData_mod_csv('./result_b.csv')
        #self.stop_anim()

    def setupUi(self, be_fit_dossier):
        be_fit_dossier.setObjectName("be_fit_dossier")
        be_fit_dossier.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(be_fit_dossier)
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
        be_fit_dossier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(be_fit_dossier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 18))
        self.menubar.setObjectName("menubar")
        be_fit_dossier.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(be_fit_dossier)
        self.statusbar.setObjectName("statusbar")
        be_fit_dossier.setStatusBar(self.statusbar)

        self.retranslateUi(be_fit_dossier)
        QtCore.QMetaObject.connectSlotsByName(be_fit_dossier)
        self.pushButton.clicked.connect(self.execDir)
        self.pushButton_2.clicked.connect(self.openFileNameDialog)


    def retranslateUi(self, be_fit_dossier):
        _translate = QtCore.QCoreApplication.translate
        be_fit_dossier.setWindowTitle(_translate("be_fit_dossier", "MainWindow"))
        self.label.setText(_translate("be_fit_dossier", "Selectionner le dossier de test"))
        self.pushButton_2.setText(_translate("be_fit_dossier", "Selectionner"))
        self.pushButton.setText(_translate("be_fit_dossier", "Tester"))
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
    be_fit_dossier = QtWidgets.QMainWindow()
    ui = Ui_be_fit_dossier()
    ui.setupUi(be_fit_dossier)
    be_fit_dossier.show()
    sys.exit(app.exec_())
