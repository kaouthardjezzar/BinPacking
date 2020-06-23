# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets , uic
from PyQt5.QtWidgets import *
import sys


from first_fit_fichier import Ui_first_fit_fichier
from first_fit_dossier import Ui_first_fit_dossier
from best_fit_fichier import Ui_best_fit_fichier
from best_fit_dossier import Ui_best_fit_dossier
from be_fit_dossier import Ui_be_fit_dossier
from be_fit_fichier import Ui_be_fit_fichier
from next_fit_fichier import Ui_next_fit_fichier
from next_fit_dossier import Ui_next_fit_dossier
from worst_fit_fichier import Ui_worst_fit_fichier
from worst_fit_dossier import Ui_worst_fit_dossier
from first_fit_dec_fichier import Ui_first_fit_dec_fichier
from first_fit_dec_dossier import Ui_first_fit_dec_dossier

from BB_fichier import Ui_BB_fichier
from BB_dossier import Ui_BB_dossier
from prog_dyn_fichier import Ui_prog_dyn_fichier
from prog_dyn_dossier import Ui_prog_dyn_dossier

from Rtabu_fichier import Ui_Rtabu_fichier
from Rtabu_dossier import Ui_Rtabu_dossier
from AG_fichier import Ui_AG_fichier
from AG_dossier import Ui_AG_dossier

from RS_fichier import Ui_RS_fichier
from RS_dossier import Ui_RS_dossier

from HRH_fichier import Ui_HRH_fichier
from HRH_dossier import Ui_HRH_dossier
from HRH_AG_RS_fichier import Ui_HRH_AG_RS_fichier
from HRH_AG_RS_dossier import Ui_HRH_AG_RS_dossier
from LTH_fichier import Ui_LTH_fichier
from LTH_dossier import Ui_LTH_dossier
from LTH2_fichier import Ui_LTH2_fichier
from LTH2_dossier import Ui_LTH2_dossier
from HTH_fichier import Ui_HTH_fichier
from HTH_dossier import Ui_HTH_dossier

from modifier_rdv import Ui_modifier_rdv


class Ui_MainWindow1(object):

    def open_first_fit_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_first_fit_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_first_fit_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_first_fit_dossier()
        self.ui.setupUi(self.window)
        # self.ui.openFileNameDialog()
        self.window.show()

    def open_best_fit_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_best_fit_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_best_fit_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_best_fit_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_next_fit_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_next_fit_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_next_fit_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_next_fit_dossier()
        self.ui.setupUi(self.window)
        # self.ui.openFileNameDialog()
        self.window.show()

    def open_be_fit_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_be_fit_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_be_fit_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_be_fit_dossier()
        self.ui.setupUi(self.window)
        # self.ui.openFileNameDialog()
        self.window.show()

    def open_worst_fit_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_worst_fit_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_worst_fit_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_worst_fit_dossier()
        self.ui.setupUi(self.window)
        # self.ui.openFileNameDialog()
        self.window.show()

    def open_first_fit_dec_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_first_fit_dec_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_first_fit_dec_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_first_fit_dec_dossier()
        self.ui.setupUi(self.window)
        # self.ui.openFileNameDialog()
        self.window.show()

    def open_BB_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BB_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_BB_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BB_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_prog_dyn_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_prog_dyn_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_prog_dyn_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_prog_dyn_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_Rtabu_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rtabu_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_Rtabu_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rtabu_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_AG_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AG_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_AG_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AG_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_RS_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RS_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_RS_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RS_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HRH_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HRH_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HRH_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HRH_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HRH_AG_RS_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HRH_AG_RS_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HRH_AG_RS_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HRH_AG_RS_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_LTH_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LTH_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_LTH_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LTH_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_LTH2_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LTH2_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_LTH2_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LTH2_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HTH_fichier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HTH_fichier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def open_HTH_dossier(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HTH_dossier()
        self.ui.setupUi(self.window)
        # self.ui.loadData_anc()
        self.window.show()

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(231, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./hp-sbp.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 18))
        self.menubar.setObjectName("menubar")
        self.menumds_lkas = QtWidgets.QMenu(self.menubar)
        self.menumds_lkas.setObjectName("menumds_lkas")
        self.menuBranch_and_Bound = QtWidgets.QMenu(self.menumds_lkas)
        self.menuBranch_and_Bound.setObjectName("menuBranch_and_Bound")
        self.menuProg_dynamique = QtWidgets.QMenu(self.menumds_lkas)
        self.menuProg_dynamique.setObjectName("menuProg_dynamique")
        self.menuGestionRDV = QtWidgets.QMenu(self.menubar)
        self.menuGestionRDV.setObjectName("menuGestionRDV")
        self.menuNext_fit = QtWidgets.QMenu(self.menuGestionRDV)
        self.menuNext_fit.setObjectName("menuNext_fit")
        self.menuBest_fit = QtWidgets.QMenu(self.menuGestionRDV)
        self.menuBest_fit.setObjectName("menuBest_fit")
        self.menuFirst_fit = QtWidgets.QMenu(self.menuGestionRDV)
        self.menuFirst_fit.setObjectName("menuFirst_fit")
        self.menuWorst_fit = QtWidgets.QMenu(self.menuGestionRDV)
        self.menuWorst_fit.setObjectName("menuWorst_fit")
        self.menuFirst_fit_decreasing = QtWidgets.QMenu(self.menuGestionRDV)
        self.menuFirst_fit_decreasing.setObjectName("menuFirst_fit_decreasing")
        self.menuConsulter_RDV = QtWidgets.QMenu(self.menubar)
        self.menuConsulter_RDV.setObjectName("menuConsulter_RDV")
        self.menu_Recuit_simul = QtWidgets.QMenu(self.menuConsulter_RDV)
        self.menu_Recuit_simul.setObjectName("menu_Recuit_simul")
        self.menuImprimerRDV = QtWidgets.QMenu(self.menubar)
        self.menuImprimerRDV.setObjectName("menuImprimerRDV")
        self.menuRecherche_tabou = QtWidgets.QMenu(self.menuImprimerRDV)
        self.menuRecherche_tabou.setObjectName("menuRecherche_tabou")
        self.menuAlgorithme_g_n_tique = QtWidgets.QMenu(self.menuImprimerRDV)
        self.menuAlgorithme_g_n_tique.setObjectName("menuAlgorithme_g_n_tique")
        self.menualgorithm_hybrid = QtWidgets.QMenu(self.menubar)
        self.menualgorithm_hybrid.setObjectName("menualgorithm_hybrid")
        self.menuHRH = QtWidgets.QMenu(self.menualgorithm_hybrid)
        self.menuHRH.setObjectName("menuHRH")
        self.menuHRH_AG_RS = QtWidgets.QMenu(self.menualgorithm_hybrid)
        self.menuHRH_AG_RS.setObjectName("menuHRH_AG_RS")
        self.menuLTH = QtWidgets.QMenu(self.menualgorithm_hybrid)
        self.menuLTH.setObjectName("menuLTH")
        self.menuHTH = QtWidgets.QMenu(self.menualgorithm_hybrid)
        self.menuHTH.setObjectName("menuHTH")
        self.menuHTH2 = QtWidgets.QMenu(self.menualgorithm_hybrid)
        self.menuHTH2.setObjectName("menuHTH2")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)
        self.actionParPatient = QtWidgets.QAction(MainWindow1)
        self.actionParPatient.setObjectName("actionParPatient")
        self.actionTester_avec_fichier_bb = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_bb.setObjectName("actionTester_avec_fichier_bb")
        self.actionTester_avec_dossier = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier.setObjectName("actionTester_avec_dossier")
        self.actionTester_avec_dossier_bb = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_bb.setObjectName("actionTester_avec_dossier_bb")
        self.actionTester_avec_fichier_pd = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_pd.setObjectName("actionTester_avec_fichier_pd")
        self.actionTester_avec_fichier_nf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_nf.setObjectName("actionTester_avec_fichier_nf")
        self.actionTester_avec_fichier_bf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_bf.setObjectName("actionTester_avec_fichier_bf")
        self.actionTester_avec_fichier_ff = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_ff.setObjectName("actionTester_avec_fichier_ff")
        self.actionTester_avec_fichier_rs = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_rs.setObjectName("actionTester_avec_fichier_rs")
        self.actionTester_avec_fichier_rt = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_rt.setObjectName("actionTester_avec_fichier_rt")
        self.actionTester_avec_fichier_ag = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_ag.setObjectName("actionTester_avec_fichier_ag")
        self.actionTester_avec_dossier_pd = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_pd.setObjectName("actionTester_avec_dossier_pd")
        self.actionTester_avec_dossier_nf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_nf.setObjectName("actionTester_avec_dossier_nf")
        self.actionTester_avec_dossier_bf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_bf.setObjectName("actionTester_avec_dossier_bf")
        self.actionTester_avec_dossier_ff = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_ff.setObjectName("actionTester_avec_dossier_ff")
        self.actionTester_avec_dossier_rs = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_rs.setObjectName("actionTester_avec_dossier_rs")
        self.actionTester_avec_dossier_rt = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_rt.setObjectName("actionTester_avec_dossier_rt")
        self.actionTester_avec_dossier_ag = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_ag.setObjectName("actionTester_avec_dossier_ag")
        self.actionTester_avec_fichier_wf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_wf.setObjectName("actionTester_avec_fichier_wf")
        self.actionTester_avec_dossier_wf = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_wf.setObjectName("actionTester_avec_dossier_wf")
        self.actionTester_avec_fichier_hrh = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_hrh.setObjectName("actionTester_avec_fichier_hrh")
        self.actionTester_avec_fichier_hrh_r = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_hrh_r.setObjectName("actionTester_avec_fichier_hrh_r")
        self.actionTester_avec_fichier_lth = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_lth.setObjectName("actionTester_avec_fichier_lth")
        self.actionTester_avec_fichier_lth2 = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_lth2.setObjectName("actionTester_avec_fichier_lth2")
        self.actionTester_avec_dossier_hrh = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_hrh.setObjectName("actionTester_avec_dossier_hrh")
        self.actionTester_avec_dossier_r = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_r.setObjectName("actionTester_avec_dossier_r")
        self.actionTester_avec_dossier_lth = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_lth.setObjectName("actionTester_avec_dossier_lth")
        self.actionTester_avec_dossier_lth2 = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_lth2.setObjectName("actionTester_avec_dossier_lth2")
        self.actionTester_avec_fichier_ff_d = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_ff_d.setObjectName("actionTester_avec_fichier_ff_d")
        self.actionTester_avec_dossier_ff_d = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_ff_d.setObjectName("actionTester_avec_dossier_ff_d")
        self.actionTester_avec_fichier_hth = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_fichier_hth.setObjectName("actionTester_avec_fichier_hth")
        self.actionTester_avec_dossier_hth = QtWidgets.QAction(MainWindow1)
        self.actionTester_avec_dossier_hth.setObjectName("actionTester_avec_dossier_hth")
        self.menuBranch_and_Bound.addAction(self.actionTester_avec_fichier_bb)
        self.menuBranch_and_Bound.addAction(self.actionTester_avec_dossier_bb)
        self.menuProg_dynamique.addAction(self.actionTester_avec_fichier_pd)
        self.menuProg_dynamique.addAction(self.actionTester_avec_dossier_pd)
        self.menumds_lkas.addAction(self.menuBranch_and_Bound.menuAction())
        self.menumds_lkas.addAction(self.menuProg_dynamique.menuAction())
        self.menuNext_fit.addAction(self.actionTester_avec_fichier_nf)
        self.menuNext_fit.addAction(self.actionTester_avec_dossier_nf)
        self.menuBest_fit.addAction(self.actionTester_avec_fichier_bf)
        self.menuBest_fit.addAction(self.actionTester_avec_dossier_bf)
        self.menuFirst_fit.addAction(self.actionTester_avec_fichier_ff)
        self.menuFirst_fit.addAction(self.actionTester_avec_dossier_ff)
        self.menuWorst_fit.addSeparator()
        self.menuWorst_fit.addAction(self.actionTester_avec_fichier_wf)
        self.menuWorst_fit.addAction(self.actionTester_avec_dossier_wf)
        self.menuFirst_fit_decreasing.addAction(self.actionTester_avec_fichier_ff_d)
        self.menuFirst_fit_decreasing.addAction(self.actionTester_avec_dossier_ff_d)
        self.menuGestionRDV.addAction(self.menuNext_fit.menuAction())
        self.menuGestionRDV.addAction(self.menuBest_fit.menuAction())
        self.menuGestionRDV.addAction(self.menuFirst_fit.menuAction())
        self.menuGestionRDV.addAction(self.menuWorst_fit.menuAction())
        self.menuGestionRDV.addAction(self.menuFirst_fit_decreasing.menuAction())
        self.menu_Recuit_simul.addAction(self.actionTester_avec_fichier_rs)
        self.menu_Recuit_simul.addAction(self.actionTester_avec_dossier_rs)
        self.menuConsulter_RDV.addAction(self.menu_Recuit_simul.menuAction())
        self.menuRecherche_tabou.addAction(self.actionTester_avec_fichier_rt)
        self.menuRecherche_tabou.addAction(self.actionTester_avec_dossier_rt)
        self.menuAlgorithme_g_n_tique.addAction(self.actionTester_avec_fichier_ag)
        self.menuAlgorithme_g_n_tique.addAction(self.actionTester_avec_dossier_ag)
        self.menuImprimerRDV.addSeparator()
        self.menuImprimerRDV.addAction(self.menuRecherche_tabou.menuAction())
        self.menuImprimerRDV.addAction(self.menuAlgorithme_g_n_tique.menuAction())
        self.menuHRH.addAction(self.actionTester_avec_fichier_hrh)
        self.menuHRH.addAction(self.actionTester_avec_dossier_hrh)
        self.menuHRH_AG_RS.addAction(self.actionTester_avec_fichier_hrh_r)
        self.menuHRH_AG_RS.addAction(self.actionTester_avec_dossier_r)
        self.menuLTH.addAction(self.actionTester_avec_fichier_lth)
        self.menuLTH.addAction(self.actionTester_avec_dossier_lth)
        self.menuHTH.addAction(self.actionTester_avec_fichier_lth2)
        self.menuHTH.addAction(self.actionTester_avec_dossier_lth2)
        self.menuHTH2.addAction(self.actionTester_avec_fichier_hth)
        self.menuHTH2.addAction(self.actionTester_avec_dossier_hth)
        self.menualgorithm_hybrid.addAction(self.menuHRH.menuAction())
        self.menualgorithm_hybrid.addAction(self.menuHRH_AG_RS.menuAction())
        self.menualgorithm_hybrid.addAction(self.menuLTH.menuAction())
        self.menualgorithm_hybrid.addAction(self.menuHTH.menuAction())
        self.menualgorithm_hybrid.addAction(self.menuHTH2.menuAction())
        self.menubar.addAction(self.menumds_lkas.menuAction())
        self.menubar.addAction(self.menuGestionRDV.menuAction())
        self.menubar.addAction(self.menuConsulter_RDV.menuAction())
        self.menubar.addAction(self.menuImprimerRDV.menuAction())
        self.menubar.addAction(self.menualgorithm_hybrid.menuAction())

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

        self.actionTester_avec_fichier_ff.triggered.connect(self.open_first_fit_fichier)
        self.actionTester_avec_dossier_ff.triggered.connect(self.open_first_fit_dossier)
        self.actionTester_avec_fichier_ff_d.triggered.connect(self.open_first_fit_dec_fichier)
        self.actionTester_avec_dossier_ff_d.triggered.connect(self.open_first_fit_dec_dossier)
        self.actionTester_avec_dossier_bf.triggered.connect(self.open_be_fit_dossier)
        self.actionTester_avec_fichier_bf.triggered.connect(self.open_be_fit_fichier)
        self.actionTester_avec_dossier_wf.triggered.connect(self.open_worst_fit_dossier)
        self.actionTester_avec_fichier_wf.triggered.connect(self.open_worst_fit_fichier)
        self.actionTester_avec_fichier_nf.triggered.connect(self.open_next_fit_fichier)
        self.actionTester_avec_dossier_nf.triggered.connect(self.open_next_fit_dossier)
        self.actionTester_avec_fichier_bb.triggered.connect(self.open_BB_fichier)
        self.actionTester_avec_dossier_bb.triggered.connect(self.open_BB_dossier)
        self.actionTester_avec_fichier_pd.triggered.connect(self.open_prog_dyn_fichier)
        self.actionTester_avec_dossier_pd.triggered.connect(self.open_prog_dyn_dossier)
        self.actionTester_avec_fichier_rt.triggered.connect(self.open_Rtabu_fichier)
        self.actionTester_avec_dossier_rt.triggered.connect(self.open_Rtabu_dossier)
        self.actionTester_avec_fichier_ag.triggered.connect(self.open_AG_fichier)
        self.actionTester_avec_dossier_ag.triggered.connect(self.open_AG_dossier)
        self.actionTester_avec_fichier_rs.triggered.connect(self.open_RS_fichier)
        self.actionTester_avec_dossier_rs.triggered.connect(self.open_RS_dossier)
        self.actionTester_avec_fichier_hrh.triggered.connect(self.open_HRH_fichier)
        self.actionTester_avec_dossier_hrh.triggered.connect(self.open_HRH_dossier)
        self.actionTester_avec_fichier_hrh_r.triggered.connect(self.open_HRH_AG_RS_fichier)
        self.actionTester_avec_dossier_r.triggered.connect(self.open_HRH_AG_RS_dossier)
        self.actionTester_avec_fichier_lth.triggered.connect(self.open_LTH_fichier)
        self.actionTester_avec_dossier_lth.triggered.connect(self.open_LTH_dossier)
        self.actionTester_avec_fichier_lth2.triggered.connect(self.open_LTH2_fichier)
        self.actionTester_avec_dossier_lth2.triggered.connect(self.open_LTH2_dossier)
        self.actionTester_avec_fichier_hth.triggered.connect(self.open_HTH_fichier)
        self.actionTester_avec_dossier_hth.triggered.connect(self.open_HTH_dossier)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.label_2.setText(_translate("MainWindow1", "APPLICATION DU PROJET OPTIMISATION"))
        self.textBrowser.setHtml(_translate("MainWindow1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">Le </span><span style=\" font-family:\'sans-serif\'; font-size:18pt; font-weight:600; color:#202122; background-color:#ffffff;\">bin packing</span><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">est </span><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#000000; background-color:#ffffff;\">un problème </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#000000; background-color:#ffffff;\">algorithmique</span><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">Il s\'agit de ranger </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">des objets avec un </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">nombre minimum </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:18pt; color:#202122; background-color:#ffffff;\">de boîtes</span></p></body></html>"))
        self.menumds_lkas.setTitle(_translate("MainWindow1", "Méthodes exactes"))
        self.menuBranch_and_Bound.setTitle(_translate("MainWindow1", "Branch and Bound"))
        self.menuProg_dynamique.setTitle(_translate("MainWindow1", "Prog dynamique"))
        self.menuGestionRDV.setTitle(_translate("MainWindow1", "Heuristiques"))
        self.menuNext_fit.setTitle(_translate("MainWindow1", "Next fit"))
        self.menuBest_fit.setTitle(_translate("MainWindow1", "Best fit"))
        self.menuFirst_fit.setTitle(_translate("MainWindow1", "First fit"))
        self.menuWorst_fit.setTitle(_translate("MainWindow1", "Worst fit"))
        self.menuFirst_fit_decreasing.setTitle(_translate("MainWindow1", "First fit decreasing"))
        self.menuConsulter_RDV.setTitle(_translate("MainWindow1", "Métaheuristiques"))
        self.menu_Recuit_simul.setTitle(_translate("MainWindow1", " Recuit simulé"))
        self.menuImprimerRDV.setTitle(_translate("MainWindow1", "Hyper-heuristiques"))
        self.menuRecherche_tabou.setTitle(_translate("MainWindow1", "Recherche tabou"))
        self.menuAlgorithme_g_n_tique.setTitle(_translate("MainWindow1", "Algorithme génétique"))
        self.menualgorithm_hybrid.setTitle(_translate("MainWindow1", " Hybrides"))
        self.menuHRH.setTitle(_translate("MainWindow1", "HRH"))
        self.menuHRH_AG_RS.setTitle(_translate("MainWindow1", "HRH_AG_RS"))
        self.menuLTH.setTitle(_translate("MainWindow1", "LTH"))
        self.menuHTH.setTitle(_translate("MainWindow1", "LTH2"))
        self.menuHTH2.setTitle(_translate("MainWindow1", "HTH"))
        self.actionParPatient.setText(_translate("MainWindow1", "ParPatient"))
        self.actionTester_avec_fichier_bb.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_bb.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_fichier_pd.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_nf.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_bf.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_ff.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_rs.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_rt.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_ag.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier_pd.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_nf.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_bf.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_ff.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_rs.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_rt.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_ag.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_fichier_wf.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier_wf.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_fichier_hrh.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_hrh_r.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_lth.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_fichier_lth2.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier_hrh.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_r.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_lth.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_dossier_lth2.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_fichier_ff_d.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier_ff_d.setText(_translate("MainWindow1", "Tester avec dossier"))
        self.actionTester_avec_fichier_hth.setText(_translate("MainWindow1", "Tester avec fichier"))
        self.actionTester_avec_dossier_hth.setText(_translate("MainWindow1", "Tester avec dossier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
