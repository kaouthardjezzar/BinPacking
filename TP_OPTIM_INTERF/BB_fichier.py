# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creer_ancien_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets , uic
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
import timeit
import bin

pathh = ''


class Ui_BB_fichier(QWidget):
    def openFileNameDialog(self):
        global pathh
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "C:/Users/Abdelbari/Desktop",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            pathh = fileName
            print(pathh,type(pathh))

    def branchAndBound(self, c, w):
        n = len(w)
        print(n,n)
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
                curN = bin.Node(wRemaining, 0, numBoxes)  # créer le premier noeud, niveau 0, nombre de boites utilisées 0

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

    def exeFile(self):
        global pathh
        a_file = open(pathh, "r")
        print(pathh,111)
        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            # line_list = stripped_line.split()
            n_liste = int(stripped_line)
            list_of_lists.append(n_liste)

        a_file.close()
        weight = list_of_lists[2:]
       # print(weight)
        c = list_of_lists[1]
        print(c)
        start = timeit.default_timer()
        C = self.branchAndBound(c,weight)
        print(C)
        stop = timeit.default_timer()
        time = stop - start
        print(C)
        print(time)
        c1 = str(C)
        self.nbr_bin.setText(c1)
        tex = time*1000
        tex1 = str(tex)
        self.t_exe.setText(tex1)
        print("nooo")
        l= list_of_lists[0]
        print(l)
        g= str(l)
        print("hi", g)
        self.items_nb.setText(g)
        r = str(c)
        print("hi",g,r)
        self.bin_cap.setText(r)

    def setupUi(self, BB_fichier):


        BB_fichier.setObjectName("BB_fichier")
        BB_fichier.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(BB_fichier)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(1000, 200))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.items_nb = QtWidgets.QTextBrowser(self.frame_8)
        self.items_nb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.items_nb.setObjectName("items_nb")
        self.gridLayout_11.addWidget(self.items_nb, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_8, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.bin_cap = QtWidgets.QTextBrowser(self.frame_9)
        self.bin_cap.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bin_cap.setObjectName("bin_cap")
        self.gridLayout_12.addWidget(self.bin_cap, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_9, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_7, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(1000, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.nbr_bin = QtWidgets.QTextBrowser(self.frame_5)
        self.nbr_bin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nbr_bin.setObjectName("nbr_bin")
        self.gridLayout_13.addWidget(self.nbr_bin, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_13.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.t_exe = QtWidgets.QTextBrowser(self.frame_6)
        self.t_exe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.t_exe.setObjectName("t_exe")
        self.gridLayout_14.addWidget(self.t_exe, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_14.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        BB_fichier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BB_fichier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 18))
        self.menubar.setObjectName("menubar")
        BB_fichier.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BB_fichier)
        self.statusbar.setObjectName("statusbar")
        BB_fichier.setStatusBar(self.statusbar)

        self.retranslateUi(BB_fichier)
        QtCore.QMetaObject.connectSlotsByName(BB_fichier)

        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.pushButton_2.clicked.connect(self.exeFile)

    def retranslateUi(self, BB_fichier):
        _translate = QtCore.QCoreApplication.translate
        BB_fichier.setWindowTitle(_translate("BB_fichier", "MainWindow"))
        self.label.setText(_translate("BB_fichier", "Selectionner le fichier de test "))
        self.pushButton.setText(_translate("BB_fichier", "Selectionner"))
        self.pushButton_2.setText(_translate("BB_fichier", "Tester"))
        self.label_4.setText(_translate("BB_fichier", "                          Item_count"))
        self.label_5.setText(_translate("BB_fichier", "                         Bin_capacity"))
        self.label_2.setText(_translate("BB_fichier", "                           Bin_count"))
        self.label_3.setText(_translate("BB_fichier", "                           Execution_time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BB_fichier = QtWidgets.QMainWindow()
    ui = Ui_BB_fichier()
    ui.setupUi(BB_fichier)
    BB_fichier.show()
    sys.exit(app.exec_())
