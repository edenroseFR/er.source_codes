import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ssis_form_UI import Ui_Form
import mysql.connector

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()



