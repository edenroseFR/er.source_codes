
from PyQt5.QtWidgets import QSizePolicy

from ssis_form_UI import *
import db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(853, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(160, 0, 805, 481))
        self.mainFrame.setStyleSheet("#mainFrame{\n"
"background-color: white;\n"
"shadow: -30x 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 30px;\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.SSISlabel = QtWidgets.QLabel(self.mainFrame)
        self.SSISlabel.setGeometry(QtCore.QRect(20, 33, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.SSISlabel.setFont(font)
        self.SSISlabel.setToolTipDuration(-2)
        self.SSISlabel.setStyleSheet("#SSISlabel{\n"
"color: rgb(0, 136, 204)\n"
"}")
        self.SSISlabel.setText("")
        self.SSISlabel.setPixmap(QtGui.QPixmap("images/ssis_icon.png"))
        self.SSISlabel.setScaledContents(True)
        self.SSISlabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.SSISlabel.setObjectName("SSISlabel")
        self.lineEdit_searchkey = QtWidgets.QLineEdit(self.mainFrame)
        self.lineEdit_searchkey.setGeometry(QtCore.QRect(120, 40, 381, 41))
        self.lineEdit_searchkey.setBaseSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_searchkey.setFont(font)
        self.lineEdit_searchkey.setStyleSheet("#lineEdit_searchkey{\n"
"border: 1px solid grey;\n"
"border-radius: 20px;\n"
"box-shadow: -4px 4px 4px 4px solid gray;\n"
"}")
        self.lineEdit_searchkey.setInputMask("")
        self.lineEdit_searchkey.setText("")
        self.lineEdit_searchkey.setMaxLength(50)
        self.lineEdit_searchkey.setFrame(True)
        self.lineEdit_searchkey.setCursorPosition(0)
        self.lineEdit_searchkey.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_searchkey.setClearButtonEnabled(False)
        self.lineEdit_searchkey.setObjectName("lineEdit_searchkey")
        self.scrollArea = QtWidgets.QScrollArea(self.mainFrame)
        self.scrollArea.setGeometry(QtCore.QRect(40, 110, 541, 341))
        self.scrollArea.setStyleSheet("#scrollArea{\n"
"border: 0px solid black;\n"
"background-color: TRANSPARENT;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 541, 341))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 541, 341))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(1,180)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEditable)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_search = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton_search.setGeometry(QtCore.QRect(455, 40, 41, 41))
        self.pushButton_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon1)
        self.pushButton_search.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_search.setFlat(True)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_addNew = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton_addNew.setGeometry(QtCore.QRect(510, 40, 111, 41))
        self.pushButton_addNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_addNew.setStyleSheet("#pushButton_addNew{\n"
"border: 0px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_addNew.setIcon(icon2)
        self.pushButton_addNew.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_addNew.setFlat(True)
        self.pushButton_addNew.setObjectName("pushButton_addNew")
        self.comboBox = QtWidgets.QComboBox(self.mainFrame)
        self.comboBox.setGeometry(QtCore.QRect(380, 50, 69, 20))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['ID', 'FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'COURSE', 'YEAR', 'GENDER'])
        self.pushButton_delete = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton_delete.setGeometry(QtCore.QRect(585, 180, 100, 41))
        self.pushButton_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet("#pushButton_addNew{\n"
"border: 0px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon3)
        self.pushButton_delete.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_delete.setFlat(True)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_edit = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton_edit.setGeometry(QtCore.QRect(585, 140, 100, 41))
        self.pushButton_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_edit.setStyleSheet("#pushButton_addNew{\n"
"border: 0px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/edit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_edit.setIcon(icon4)
        self.pushButton_edit.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_edit.setFlat(True)
        self.pushButton_edit.setObjectName("pushButton_delete_2")
        self.pushButton_sort = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton_sort.setGeometry(QtCore.QRect(585, 220, 100, 41))
        self.pushButton_sort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sort.setStyleSheet("#pushButton_addNew{\n"
"border: 0px;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/sort_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon5)
        self.pushButton_sort.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_sort.setFlat(True)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.sortLayout = QtWidgets.QFrame(self.mainFrame)
        self.sortLayout.setEnabled(False)
        self.sortLayout.setGeometry(QtCore.QRect(600, 260, 95, 130))
        self.sortLayout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sortLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sortLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sortLayout.setObjectName("sortLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sortLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.id = QtWidgets.QPushButton(self.sortLayout)
        self.id.setObjectName("id")
        self.verticalLayout.addWidget(self.id)
        self.lastname = QtWidgets.QPushButton(self.sortLayout)
        self.lastname.setObjectName("lastname")
        self.verticalLayout.addWidget(self.lastname)
        self.course = QtWidgets.QPushButton(self.sortLayout)
        self.course.setObjectName("course")
        self.verticalLayout.addWidget(self.course)
        self.yearlevel = QtWidgets.QPushButton(self.sortLayout)
        self.yearlevel.setObjectName("yearlevel")
        self.verticalLayout.addWidget(self.yearlevel)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 141, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_account = QtWidgets.QLabel(self.frame)
        self.label_account.setGeometry(QtCore.QRect(0, 350, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label_account.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.label_account.setFont(font)
        self.label_account.setStyleSheet("#label_account{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"    text-decoration: underline;\n"
"    text-decoration: underline;\n"
"color: white;\n"
"\n"
"}")
        self.label_account.setObjectName("label_account")
        self.pushButton_changeUsername = QtWidgets.QPushButton(self.frame)
        self.pushButton_changeUsername.setGeometry(QtCore.QRect(4, 370, 131, 23))
        self.pushButton_changeUsername.setStyleSheet("#pushButton_changeUsername {\n"
"color: white;\n"
"}")
        self.pushButton_changeUsername.setFlat(True)
        self.pushButton_changeUsername.setObjectName("pushButton_changeUsername")
        self.pushButton_changePassword = QtWidgets.QPushButton(self.frame)
        self.pushButton_changePassword.setGeometry(QtCore.QRect(0, 390, 141, 23))
        self.pushButton_changePassword.setStyleSheet("#pushButton_changePassword {\n"
"color: white;\n"
"}")
        self.pushButton_changePassword.setFlat(True)
        self.pushButton_changePassword.setObjectName("pushButton_changePassword")
        self.label_count = QtWidgets.QLabel(self.frame)
        self.label_count.setGeometry(QtCore.QRect(6, 20, 131, 20))
        self.label_count.setStyleSheet("#label_count{\n"
"color: white;\n"
"font: 75 14pt \"Perpetua\";\n"
"}")
        self.label_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_count.setObjectName("label_count")
        self.graphicsView_students = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_students.setGeometry(QtCore.QRect(20, 50, 111, 101))
        self.graphicsView_students.setStyleSheet("#graphicsView_students{\n"
"border: 2px;\n"
"border-radius: 20px;\n"
"}")
        self.graphicsView_students.setObjectName("graphicsView_students")
        self.label_students = QtWidgets.QLabel(self.frame)
        self.label_students.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label_students.setStyleSheet("#label_students {\n"
"color:rgb(42, 0, 127);\n"
"}")
        self.label_students.setObjectName("label_students")
        self.graphicsView_courses = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_courses.setGeometry(QtCore.QRect(20, 170, 111, 101))
        self.graphicsView_courses.setStyleSheet("#graphicsView_courses{\n"
"border: 2px;\n"
"border-radius: 20px;\n"
"}")
        self.graphicsView_courses.setObjectName("graphicsView_courses")
        self.label_courses = QtWidgets.QLabel(self.frame)
        self.label_courses.setGeometry(QtCore.QRect(30, 180, 47, 13))
        self.label_courses.setStyleSheet("#label_courses {\n"
"color:rgb(42, 0, 127);\n"
"}")
        self.label_courses.setObjectName("label_courses")
        self.pushButton_LOGOUT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LOGOUT.setGeometry(QtCore.QRect(10, 10, 81, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_LOGOUT.setFont(font)
        self.pushButton_LOGOUT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LOGOUT.setStyleSheet("#pushButton_LOGOUT{\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LOGOUT.setIcon(icon6)
        self.pushButton_LOGOUT.setFlat(True)
        self.pushButton_LOGOUT.setObjectName("pushButton_LOGOUT")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 30, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.raise_()
        self.mainFrame.raise_()
        self.frame.raise_()
        self.pushButton_LOGOUT.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_sort.clicked['bool'].connect(self.sortLayout.setDisabled)
        self.pushButton_LOGOUT.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information System"))
        self.SSISlabel.setToolTip(_translate("MainWindow", "Simple Student Information System"))
        self.lineEdit_searchkey.setPlaceholderText(_translate("MainWindow", "Search"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Year Level"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_search.setToolTip(_translate("MainWindow", "<html><head/><body><p>Search</p></body></html>"))
        self.pushButton_addNew.setText(_translate("MainWindow", "Add New"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_edit.setText(_translate("MainWindow", "Edit"))
        self.pushButton_sort.setText(_translate("MainWindow", "Sort"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.lastname.setText(_translate("MainWindow", "Last Name"))
        self.course.setText(_translate("MainWindow", "Course"))
        self.yearlevel.setText(_translate("MainWindow", "Year Level"))
        self.label_account.setText(_translate("MainWindow", "Account Settings"))
        self.pushButton_changeUsername.setText(_translate("MainWindow", "Change Username"))
        self.pushButton_changePassword.setText(_translate("MainWindow", "Change Password"))
        self.label_count.setText(_translate("MainWindow", "Counts"))
        self.label_students.setText(_translate("MainWindow", "Students"))
        self.label_courses.setText(_translate("MainWindow", "Courses"))
        self.pushButton_LOGOUT.setText(_translate("MainWindow", "LOGOUT"))


class Ui_Form(object):
    def setupUi(self, Form, parent = None, edit = False, studentID = None):
        self.p = parent
        self.edit = edit

        # main widget
        Form.setObjectName("Form")
        Form.resize(236, 394)
        Form.setStyleSheet("#Form{\n"
                           "background-color: white;\n"
                           "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../pyqt5/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        # rectangle header
        self.header = QtWidgets.QWidget(Form)
        self.header.setObjectName("header")
        self.header.setGeometry(QtCore.QRect(0, 0, 240, 101))
        self.header.setStyleSheet("#header{\n"
                                "background-color: rgb(0, 170, 255);\n"
                                "}")

        # layout management
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 150, 201, 186))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")

        if self.edit:
            pass



        # student id
        self.studentIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.studentIDLabel.setObjectName("studentIDLabel")
        self.gridLayout.addWidget(self.studentIDLabel, 0, 0, 1, 1)
        self.studentIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.studentIDLineEdit.setObjectName("studentIDLineEdit")
        self.gridLayout.addWidget(self.studentIDLineEdit, 0, 1, 1, 1)
        self.studentIDLineEdit.setFocus()

        # first name
        self.firstNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.gridLayout.addWidget(self.firstNameLabel, 1, 0, 1, 1)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.gridLayout.addWidget(self.firstNameLineEdit, 1, 1, 1, 1)

        # middle name
        self.middleNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.middleNameLabel.setObjectName("middleNameLabel")
        self.gridLayout.addWidget(self.middleNameLabel, 2, 0, 1, 1)
        self.middleNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.middleNameLineEdit.setObjectName("middleNameLineEdit")
        self.gridLayout.addWidget(self.middleNameLineEdit, 2, 1, 1, 1)

        # last name
        self.lastNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.gridLayout.addWidget(self.lastNameLabel, 3, 0, 1, 1)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.gridLayout.addWidget(self.lastNameLineEdit, 3, 1, 1, 1)

        # course
        self.courseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.courseLabel.setObjectName("courseLabel")
        self.gridLayout.addWidget(self.courseLabel, 4, 0, 1, 1)
        self.courseComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.courseComboBox.setObjectName("courseComboBox")
        self.courseComboBox.setEditable(True)
        self.courseComboBox.setPlaceholderText('Ex. BSCS')
        self.gridLayout.addWidget(self.courseComboBox, 4, 1, 1, 1)

        # year level
        self.yearLevelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yearLevelLabel.setObjectName("yearLevelLabel")
        self.gridLayout.addWidget(self.yearLevelLabel, 5, 0, 1, 1)
        self.yearLevelComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.yearLevelComboBox.setObjectName("yearLevelComboBox")
        self.yearLevelComboBox.addItems(['1','2','3','4','5'])
        self.gridLayout.addWidget(self.yearLevelComboBox, 5, 1, 1, 1)

        # gender
        self.genderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.gridLayout.addWidget(self.genderLabel, 6, 0, 1, 1)
        self.genderComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItems(['Choose Gender', 'Male', 'Female', 'Lesbian', 'Gay', 'Bisexual', 'Transgender', 'Unknown'])
        self.gridLayout.addWidget(self.genderComboBox, 6, 1, 1, 1)

        # student picture
        self.label_pic = QtWidgets.QLabel(Form)
        self.label_pic.setGeometry(QtCore.QRect(70, 40, 101, 100))
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap("../../pyqt5/images/changeusername_icon.png"))
        self.label_pic.setScaledContents(True)
        self.label_pic.setWordWrap(False)
        self.label_pic.setObjectName("label_pic")
        self.pushButton_editPic = QtWidgets.QPushButton(Form)
        self.pushButton_editPic.setGeometry(QtCore.QRect(170, 110, 31, 23))
        self.pushButton_editPic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../pyqt5/images/edit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editPic.setIcon(icon1)
        self.pushButton_editPic.setFlat(True)
        self.pushButton_editPic.setObjectName("pushButton_editPic")

        # button
        self.pushButton_AddStudent = QtWidgets.QPushButton(Form)
        self.pushButton_AddStudent.setGeometry(QtCore.QRect(20, 350, 201, 23))
        self.pushButton_AddStudent.setObjectName("pushButton_AddStudent")

        # add all course_code as items of course_comboBox
        query = 'SELECT course_code FROM courses'
        db.cursor.execute(query)
        courses = list(map(str, db.cursor.fetchall()))
        courses = [i.strip("('),") for i in courses]
        self.courseComboBox.addItems(courses)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def b(self):
        self.p.fillTable()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add New"))
        self.studentIDLabel.setText(_translate("Form", "studentID"))
        self.firstNameLabel.setText(_translate("Form", "First Name"))
        self.middleNameLabel.setText(_translate("Form", "Middle Name"))
        self.lastNameLabel.setText(_translate("Form", "Last Name"))
        self.courseLabel.setText(_translate("Form", "Course"))
        self.yearLevelLabel.setText(_translate("Form", "Year Level"))
        self.genderLabel.setText(_translate("Form", "Gender"))
        self.pushButton_AddStudent.setText(_translate("Form", "Add Student"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
