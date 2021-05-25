import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ssis_signup_UI import Ui_Form
import mysql.connector

class SignUp(QtWidgets.QWidget):
    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()
    def initializeUI(self):
        self.database = mysql.connector.connect(host='localhost', user='root', password='edenrose',database='student_information')
        self.mycursor = self.database.cursor()

        self.ui.pushButton_login.clicked.connect(self.checkCredentials)

    def checkCredentials(self):
        firstname = self.ui.label_firstname.text()
        middlename = self.ui.label_lastname.text()
        lastname = self.ui.label_lastname.text()
        username = self.ui.label_username.text()
        password = self.ui.label_password.text()





app = QtWidgets.QApplication(sys.argv)
window = SignUp()
sys.exit(app.exec())