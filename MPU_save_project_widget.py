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

from MPU_save_project_validation_widget import * 

class MPU_save_project_widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()

        self.gb = QGroupBox(self)
        self.core = ""
        self.project_name           = QLineEdit(self.gb)
        self.button_save_project    = QPushButton("Сохранить", self.gb)
        self.button_cancel          = QPushButton("Отмена", self.gb)
        self.list_project_names     = os.listdir(".config_MPU")

        self.button_save_project.clicked.connect(self.slot_button_save_project)
        self.button_cancel.clicked.connect(self.slot_button_cancel)

    #     self.get_all_project_names()

    # def get_all_project_names(self):
    #     self.list_project_names = os.listdir(".config")
    #     print(self.list_project_names)
        self.project_validation_window = MPU_save_project_validation_widget()
        self.project_validation_window.set_main(self)

        self.resize(430,140)

    def set_core(self, Core):
        self.core = Core
        self.project_validation_window.set_core(Core)

    def slot_button_save_project(self):
        text = self.project_name.text()


        if(text in self.list_project_names):
            self.project_validation_window.show()
        else:
            self.core.save_project(text)

    def slot_button_cancel(self):
        self.close()
    def set_project_name(self, project_name):
        self.project_name.setText(project_name)
        
    def rewrite_project(self):
        print(self.project_name.text())
        self.core.save_project(self.project_name.text())
        self.close()

    def resizeEvent(self, a0):
        self.gb.setGeometry(5,5, self.width() - 10, self.height() - 10)
        self.project_name.setGeometry(5,5, self.gb.width() - 10, 35)
        self.button_save_project.setGeometry(5 , self.project_name.y() + self.project_name.height() + 5, int((self.gb.width() - 20)/2), 35)
        self.button_cancel.setGeometry(int((self.gb.width() - 20)/2) + 15 , self.button_save_project.y(), int((self.gb.width() - 20)/2), 35)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MPU_save_project_widget()
    dl.show()
    sys.exit(app.exec_())