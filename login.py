import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ssis_login_UI import Ui_Form
import mysql.connector

class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()
    def initializeUI(self):
        self.database = mysql.connector.connect (host = 'localhost', user = 'root', password = 'edenrose', database = 'student_information')
        self.mycursor = self.database.cursor()

        self.ui.pushButton_login.clicked.connect(self.checkCredentials)

    def checkCredentials(self):
        entered_username = self.ui.lineEdit_username.text()
        entered_password = self.ui.lineEdit_password.text()

        query = "SELECT username, password FROM student_information.user"
        self.mycursor.execute(query)
        





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec())