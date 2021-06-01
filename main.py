import sys

from PyQt5.QtWidgets import QTableWidgetItem

import re
from PyQt5 import QtCore, QtGui, QtWidgets
from ssis_main_UI import Ui_MainWindow
from ssis_login_UI import Ui_Login
from ssis_signup_UI import Ui_SignUp
from form import Ui_Form
import db

class Login(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.pushButton_login.clicked.connect(self.checkCredentials)
        self.ui.pushButton_signup.clicked.connect(self.goto_SignUpWindow)

    def checkCredentials(self):
        entered_username = self.ui.lineEdit_username.text()
        entered_password = self.ui.lineEdit_password.text()

        query = ('SELECT username, password FROM user WHERE username = "%s" and password = "%s";' % (entered_username, entered_password))
        db.cursor.execute(query)
        result = db.cursor.fetchall()

        if (entered_username,entered_password) in result:
            self.goto_MainWindow()
        else:
            self.goto_SignUpWindow()

    def goto_MainWindow(self):
        self.newWin = MainWindow()
        self.newWin.show()
        self.close()

    def goto_SignUpWindow(self):
        self.newWin = SignUp()
        self.newWin.show()
        self.close()


class SignUp(QtWidgets.QWidget, Ui_SignUp):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.pushButton_signup.clicked.connect(self.checkDetails)
        self.ui.pushButton_login.clicked.connect(self.goto_LoginWindow)

    def checkDetails(self):
        first_name = self.ui.firstname.text()
        last_name = self.ui.lastname.text()
        username = self.ui.username.text()
        password = self.ui.password.text()

        if first_name and last_name and username and password:
            query = ('SELECT username FROM user WHERE username = "%s";' % username)
            db.cursor.execute(query)
            if len(db.cursor.fetchall()) == 0:
                self.addNewUser(first_name, last_name, username, password)
            else:
                QtWidgets.QMessageBox.information(self, "Oops!", "Username already taken.", QtWidgets.QMessageBox.Ok)
                self.ui.username.setFocus()
        else:
            print('here')
            QtWidgets.QMessageBox.information(self, "Incomplete Information", "Hi there human! \nSorry, but they are all necessary information.\nPlease fill them all up. Thank you!",
                                              QtWidgets.QMessageBox.Ok)

    def addNewUser(self, fname, lname, username, password):
        query = ('INSERT INTO `user` (`first_name`, `last_name`, `username`, `password`) VALUES("%s","%s","%s","%s");' %(fname, lname, username, password))
        db.cursor.execute(query)
        db.database.commit()
        self.goto_LoginWindow()

    def goto_LoginWindow(self):
        self.newWin = Login()
        self.newWin.show()
        self.close()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.pushButton_addNew.clicked.connect(self.goto_addStudent)
        self.fillTable()

    def fillTable(self):
        students = db.students()
        row = 0
        self.ui.tableWidget.setRowCount(len(students))
        for student in students:
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(student[0]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(student[1]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(student[2]))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(student[3])))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(student[4])))

            row += 1
        return

    def goto_addStudent(self):
        self.popUp = AddStudent(self)
        self.popUp.show()


class AddStudent(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(AddStudent, self).__init__(parent)
        self.p = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.pushButton.clicked.connect(self.checkInformation)
        self.ui.comboBox.addItems(db.get_courses())
        self.ui.comboBox_2.addItems(['1','2','3','4','5','6'])
        self.ui.comboBox_3.addItems(['Male','Female','Lesbian','Gay','Bisexual','Transgender','Unknown'])

    def checkInformation(self):
        id = self.ui.lineEdit.text()
        first_name = self.ui.lineEdit_2.text()
        middle_name = self.ui.lineEdit_3.text()
        last_name = self.ui.lineEdit_6.text()
        course = self.ui.comboBox.currentText()
        year = str(self.ui.comboBox_2.currentText())
        gender = str(self.ui.comboBox_3.currentText())
        if id and first_name and middle_name and last_name and course and year and gender:
            db.add_student(id,first_name,middle_name,last_name,course,year,gender)
            self.p.fillTable()




app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
