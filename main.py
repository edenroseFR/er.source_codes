import sys

from PyQt5.QtWidgets import QTableWidgetItem
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ssis_main_UI import Ui_MainWindow
from ssis_login_UI import Ui_Login
from ssis_signup_UI import Ui_SignUp
from form import Ui_Form
import messagebox
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
        self.ui.pushButton_search.clicked.connect(self.search_student)
        self.ui.pushButton_edit.clicked.connect(self.edit_student)
        self.ui.pushButton_delete.clicked.connect(self.delete_student)
        self.fillTable()


    def fillTable(self, students=db.students()):
        row = 0
        self.ui.tableWidget.setRowCount(len(students))
        for student in students:
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(student[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(student[1])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(student[2])))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(student[3])))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(student[4])))

            row += 1

    def goto_addStudent(self):
        self.popUp = AddStudent(self, winName='Add New Student')
        self.popUp.show()

    def search_student(self):
        type = self.ui.comboBox.currentText()
        key = str(self.ui.lineEdit_searchkey.text())
        if type == 'ID':
            result = db.students('SELECT * FROM students where students_id = "%s"' % key)
        elif type == 'FIRST NAME':
            result = db.students('SELECT * FROM students where first_name = "%s"' % key)
        elif type == 'MIDDLE NAME':
            result = db.students('SELECT * FROM students where middle_name = "%s"' % key)
        elif type == 'LAST NAME':
            result = db.students('SELECT * FROM students where last_name = "%s"' % key)
        elif type == 'COURSE':
            result = db.students('SELECT * FROM students where fk_course_code = "%s"' % key)
        elif type == 'YEAR':
            result = db.students('SELECT * FROM students where year_level = "%s"' % int(key))
        elif type == 'GENDER':
            result = db.students('SELECT * FROM students where gender = "%s"' % key)

        if len(result) == 0:
            messagebox.noResult(self)
            self.fillTable()
        else:
            self.fillTable(students=result)

    def edit_student(self):
        if self.ui.tableWidget.selectedItems() != []:
            selected_id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()
            self.openForm = AddStudent(self, mode='edit', studID=selected_id, winName='Edit Student')
            self.openForm.show()

    def delete_student(self):
        if self.ui.tableWidget.selectedItems() != []:
            selected_id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()
            selected_name = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),1).text()
            if messagebox.confirmDelete(self, selected_name) == 'continue':
                db.delete_student(selected_id)
                self.fillTable(db.students())


class AddStudent(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None, mode=None, studID=None, winName=None):
        super(AddStudent, self).__init__(parent)
        self.p = parent
        self.mode = mode
        self.studID = studID
        self.ui = Ui_Form()
        self.ui.setupUi(self, parent, mode, studID, winName)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.comboBox.addItems(db.get_courses())
        self.ui.comboBox.setCurrentText('')
        self.ui.comboBox_2.addItems(['', '1','2','3','4','5','6'])
        self.ui.comboBox_3.addItems(['', 'Male','Female','Lesbian','Gay','Bisexual','Transgender','Unknown'])

        if self.mode == 'edit':
            details = db.get_student(self.ui.studID)
            self.ui.lineEdit.setText(self.ui.studID)
            self.ui.lineEdit.setDisabled(True)

            self.ui.lineEdit_2.setText(details[1])
            self.ui.lineEdit_3.setText(details[2])
            self.ui.lineEdit_6.setText(details[3])

            self.ui.comboBox.setCurrentText(details[4])
            self.ui.comboBox_2.setCurrentText(str(details[5]))
            self.ui.comboBox_3.setCurrentText(details[6])

            self.ui.pushButton.setText('Update Student')
            self.ui.pushButton.clicked.connect(self.__edit)
        else:
            self.ui.pushButton.clicked.connect(self.checkInformation)

    def __edit(self):
        self.checkInformation(mode='edit')



    def checkInformation(self, mode=None):
        d=mode
        id = self.ui.lineEdit.text()
        first_name = self.ui.lineEdit_2.text()
        middle_name = self.ui.lineEdit_3.text()
        last_name = self.ui.lineEdit_6.text()
        course = self.ui.comboBox.currentText()
        year = str(self.ui.comboBox_2.currentText())
        gender = str(self.ui.comboBox_3.currentText())
        if id and first_name and last_name and course and year and gender:

            if not d:
                db.add_student(id, first_name, middle_name, last_name, course, year, gender)
                messagebox.addSuccessful(MainWindow())
                self.close()
            else:
                db.update_student(self.studID, first_name, middle_name, last_name, course, year, gender)
                self.close()

            self.p.fillTable(students=db.students())






app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
