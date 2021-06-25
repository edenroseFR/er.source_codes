import sys

from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from ssis_main_UI import Ui_MainWindow
from ssis_login_UI import Ui_Login
from ssis_signup_UI import Ui_SignUp
from form import Ui_Form
from courseForm import Ui_courseForm
import messagebox
import sort
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
        self.ui.pushButton_changePassword.close()
        self.ui.pushButton_changeUsername.close()
        self.ui.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.ui.pushButton_addNew.clicked.connect(self.goto_addStudent)
        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.pushButton_edit.clicked.connect(self.edit_student)
        self.ui.pushButton_delete.clicked.connect(self.delete_student)
        self.ui.pushButton_LOGOUT.clicked.connect(self.logout)
        self.ui.id.clicked.connect(self.sort_by_id)
        self.ui.lastname.clicked.connect(self.sort_by_lastname)
        self.ui.course.clicked.connect(self.sort_by_course)
        self.ui.yearlevel.clicked.connect(self.sort_by_yearlevel)
        self.ui.courseSection.clicked.connect(self.show_courses)
        self.ui.studentSection.clicked.connect(self.show_students)
        self.ui.pushButton_changeUsername.clicked.connect(self.change_username)
        self.fillTable(students=db.students())


    def fillTable(self, students=None, courses=None):
        row = 0

        if students:
            self.ui.tableWidget.setRowCount(len(students))
            for each in students:
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(each[0])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(each[1])))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(each[2])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(each[3])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(each[4])))

                row += 1
        elif courses:
            self.ui.tableWidget.setRowCount(len(courses))
            for each in courses:
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(each[0])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(each[1])))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(each[2])))

                row += 1

        self.ui.studentSection.setText('Students: ' + str(len(db.students())))
        self.ui.courseSection.setText('Courses: ' + str(len(db.get_courses())))


    def goto_addStudent(self):
        self.popUp = AddStudent(self, winName='Add New Student')
        self.popUp.show()

    def logout(self):
        self.close()
        self.login = Login()
        self.login.show()

    def change_username(self):
        print('here')

    def sort_by_id(self):
        sorted = sort.byID()
        self.fillTable(students=sorted)

    def sort_by_lastname(self):
        sorted = sort.byLastName()
        self.fillTable(students=sorted)

    def sort_by_course(self):
        sorted = sort.bycourse()
        self.fillTable(students=sorted)

    def sort_by_yearlevel(self):
        sorted = sort.byYearLevel()
        self.fillTable(students=sorted)

    def show_courses(self):
        self.t_header = self.ui.tableWidget.horizontalHeader()
        self.t_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.t_header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.t_header.hideSection(3)
        self.t_header.hideSection(4)
        col1 = self.ui.tableWidget.horizontalHeaderItem(0)
        col1.setText('COURSE CODE')
        col2 = self.ui.tableWidget.horizontalHeaderItem(1)
        col2.setText('COURSE NAME')
        col3 = self.ui.tableWidget.horizontalHeaderItem(2)
        col3.setText('ENROLLED STUDENT')

        self.fillTable(courses= db.courses())

        self.ui.pushButton_delete.disconnect()
        self.ui.pushButton_delete.clicked.connect(self.del_course)
        self.ui.pushButton_edit.disconnect()
        self.ui.pushButton_edit.clicked.connect(self.edit_course)
        self.ui.pushButton_addNew.setDisabled(True)
        self.ui.pushButton_sort.setDisabled(True)
        self.ui.pushButton_search.disconnect()
        self.ui.pushButton_search.clicked.connect(self.course_result)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(['code', 'name'])


    def course_result(self):
        self.key = self.ui.lineEdit_searchkey.text()
        self.result = db.search_course(key=self.key, comboBox=self.ui.comboBox.currentText())
        self.fillTable(courses=self.result)

    def del_course(self):
        enrolled = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text())
        selected_ccode = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
        selected_cname = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
        if self.ui.tableWidget.selectedItems() != [] and enrolled == 0:
            if messagebox.confirmDelete(self, selected_cname) == 'continue':
                db.delete_course(selected_ccode)
                self.fillTable(courses=db.courses())

        elif enrolled > 0:
            messagebox.cantDeleteCourse(self, selected_cname, enrolled)

    def edit_course(self):
        ccode = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
        self.courseForm = CourseForm(self, mode='edit',course_code=ccode, winName='Edit Course')
        self.courseForm.show()



    def show_students(self):
        self.t_header = self.ui.tableWidget.horizontalHeader()
        self.t_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.t_header.setSectionResizeMode(4, QHeaderView.Stretch)
        self.ui.tableWidget.setColumnWidth(2, 50)
        self.ui.tableWidget.setColumnWidth(3, 70)
        col1 = self.ui.tableWidget.horizontalHeaderItem(0)
        col1.setText('Student ID')
        col2 = self.ui.tableWidget.horizontalHeaderItem(1)
        col2.setText('Name')
        col3 = self.ui.tableWidget.horizontalHeaderItem(2)
        col3.setText('Course')
        self.t_header.showSection(3)
        self.t_header.showSection(4)

        self.fillTable(students=db.students())
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(['ID', 'FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'COURSE', 'YEAR', 'GENDER'])




    def search(self):
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
        elif type == 'code':
            result = db.courses('SELECT * FROM courses where course_code = "%s"' % key)
        elif type == 'name':
            result = db.courses('SELECT * FROM courses where course_name = "%s"' % key)


        if len(result) == 0:
            messagebox.noResult(self)
            self.fillTable(students=db.students())
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
                self.fillTable(students=db.students())


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
        self.ui.lineEdit.setPlaceholderText('YYYY-NNNN')
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
        d = mode
        id = self.ui.lineEdit.text()
        first_name = self.ui.lineEdit_2.text()
        middle_name = self.ui.lineEdit_3.text()
        last_name = self.ui.lineEdit_6.text()
        course = self.ui.comboBox.currentText()
        year = str(self.ui.comboBox_2.currentText())
        gender = str(self.ui.comboBox_3.currentText())
        self.pattern = '^[0-9]{4}-[0-9]{4}$'
        if (re.search(self.pattern, id) and id not in db.get_IDs()) and first_name and last_name \
                and course in db.get_courses() and year and gender:

            if not d:
                db.add_student(id, first_name, middle_name, last_name, course, year, gender)
                self.close()
                messagebox.addSuccessful(MainWindow())
            else:
                db.update_student(self.studID, first_name, middle_name, last_name, course, year, gender)
                self.close()

            self.p.fillTable(students=db.students())

        elif not re.search(self.pattern, id):
            messagebox.wrongPattern(self)

        elif id in db.get_IDs():
            messagebox.idAlreadyTaken(self, studID=id)

        elif not first_name or not last_name or not year or not gender:
            messagebox.incompleteInfo(self)

        elif course not in db.get_courses():
            if messagebox.addCoursePrompt(self) == 'continue':
                self.addCourse = CourseForm(MainWindow(), mode = 'add', course_code=course, winName='Add Course')
                self.addCourse.show()


class CourseForm(QtWidgets.QMainWindow, Ui_courseForm):
    def __init__(self, parent=None, mode=None, course_code=None, winName=None):
        super(CourseForm, self).__init__(parent)
        self.p = parent
        self.mode = mode

        self.coursecode = course_code
        self.winName = winName

        self.ui = Ui_courseForm()
        self.ui.setupUi(self, parent, mode, course_code, winName)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.coursecode.setText(self.coursecode)
        self.ui.pushButton.cursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        if self.mode == 'add':
            self.ui.pushButton.clicked.connect(self.checkInformation)
        elif self.mode == 'edit':
            self.ui.lineEdit.setText(db.get_courseName(code=self.coursecode))
            self.ui.pushButton.clicked.connect(self.edit_name)


    def edit_name(self):
        self.checkInformation(mode='edit')


    def checkInformation(self, mode='add'):
        cname = self.ui.lineEdit.text()
        if cname:
            if mode == 'add':
                if messagebox.confirmAddCourse(self, self.coursecode, cname) == 'continue':
                    db.add_course(self.coursecode, cname)
                    self.p.fillTable(courses=db.courses())
                    self.close()
                    messagebox.courseAdded(self)
            elif mode == 'edit':
                db.update_course(self.coursecode, cname)
                self.p.fillTable(courses=db.courses())
                self.close()

        else:
            messagebox.incompleteInfo(self)







app = QtWidgets.QApplication(sys.argv)
win = Login()
win.show()
sys.exit(app.exec_())
