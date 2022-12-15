


import psycopg2
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore, QtGui, QtWidgets , uic
from PyQt5.QtWidgets import QFileDialog, QMenuBar, QAction, QPushButton
from PyQt5.QtCore import Qt , QTimer
from PyQt5.QtGui import QColor , QPen, QBrush
from QCustomPlot2 import * 
import sys
import os
import shutil
import cups
from datetime import datetime
import time
import scipy.stats as sps
import itertools as iter


class MPU_save_project_validation_widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()

        self.gb = QGroupBox(self)
        self.core = ""
        self.main = ""
        self.label_validation1      = QLabel("Файл с таким именем существует", self.gb)
        self.label_validation2      = QLabel("Вы действительно хотите его заменить?", self.gb)
        self.button_save_project    = QPushButton("Заменить", self.gb)
        self.button_cancel          = QPushButton("Отмена", self.gb)
         

        self.label_validation1.setFont(QFont("Times", 18))
        self.label_validation2.setFont(QFont("Times", 18))
        self.label_validation1.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.label_validation2.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        # self.list_project_names     = os.listdir(".config")

        self.button_save_project.clicked.connect(self.slot_button_save_project)
        self.button_cancel.clicked.connect(self.slot_button_cancel)

        self.resize(430,140)
    #     self.get_all_project_names()

    # def get_all_project_names(self):
    #     self.list_project_names = os.listdir(".config")
    #     print(self.list_project_names)

    def set_core(self, Core):
        self.core = Core
    def set_main(self, main):
        self.main = main

    def slot_button_save_project(self):
        # text = self.project_name.text()
        print("Rewrite_project")
        if(self.main != ""):
            self.main.rewrite_project()
        
        self.close()
        # print("Да")

    def slot_button_cancel(self):
        self.close()

    def resizeEvent(self, a0):
        self.gb.setGeometry(5,5, self.width() - 10, self.height() - 10)
        self.label_validation1.setGeometry(5,5, self.gb.width() - 10, 35)
        self.label_validation2.setGeometry(5, self.label_validation1.y() + self.label_validation1.height() + 5, self.gb.width() - 10, 35)
        self.button_save_project.setGeometry(5 , self.label_validation2.y() + self.label_validation2.height() + 5, int((self.gb.width() - 20)/2), 35)
        self.button_cancel.setGeometry(int((self.gb.width() - 20)/2) + 15 , self.button_save_project.y(), int((self.gb.width() - 20)/2), 35)

        print(f"{self.width()} | {self.height()}")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MPU_save_project_validation_widget()
    dl.show()
    sys.exit(app.exec_())