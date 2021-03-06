# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(805, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form {\n"
"background-color: #daecf4;\n"
"}")
        self.label_SSIS = QtWidgets.QLabel(Form)
        self.label_SSIS.setGeometry(QtCore.QRect(30, 150, 461, 261))
        self.label_SSIS.setText("")
        self.label_SSIS.setPixmap(QtGui.QPixmap("images/login_text.png"))
        self.label_SSIS.setScaledContents(True)
        self.label_SSIS.setObjectName("label_SSIS")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 20, 521, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/signup-template.png"))
        self.label.setObjectName("label")
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(410, 310, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("#label_username{\n"
"color: #128785;\n"
"}")
        self.label_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.line2 = QtWidgets.QFrame(Form)
        self.line2.setGeometry(QtCore.QRect(510, 359, 191, 16))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QFrame(Form)
        self.line1.setGeometry(QtCore.QRect(510, 320, 191, 16))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(410, 350, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("#label_password{\n"
"color: #128785;\n"
"}")
        self.label_password.setObjectName("label_password")
        self.pushButton_signup = QtWidgets.QPushButton(Form)
        self.pushButton_signup.setGeometry(QtCore.QRect(510, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_signup.setStyleSheet("#pushButton_signup{\n"
"color: black;\n"
"background-color: white;\n"
"border: 1px solid #0a9cad;\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_signup.setFlat(False)
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.line1_2 = QtWidgets.QFrame(Form)
        self.line1_2.setGeometry(QtCore.QRect(510, 240, 191, 16))
        self.line1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1_2.setObjectName("line1_2")
        self.label_lastname = QtWidgets.QLabel(Form)
        self.label_lastname.setGeometry(QtCore.QRect(410, 270, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lastname.setFont(font)
        self.label_lastname.setStyleSheet("#label_lastname{\n"
"color: #128785;\n"
"}")
        self.label_lastname.setObjectName("label_lastname")
        self.label_firstname = QtWidgets.QLabel(Form)
        self.label_firstname.setGeometry(QtCore.QRect(410, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_firstname.setFont(font)
        self.label_firstname.setStyleSheet("#label_firstname{\n"
"color: #128785;\n"
"}")
        self.label_firstname.setObjectName("label_firstname")
        self.line2_2 = QtWidgets.QFrame(Form)
        self.line2_2.setGeometry(QtCore.QRect(510, 279, 191, 16))
        self.line2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2_2.setObjectName("line2_2")
        self.firstname = QtWidgets.QLineEdit(Form)
        self.firstname.setGeometry(QtCore.QRect(510, 220, 191, 25))
        self.firstname.setStyleSheet("#firstname{\n"
"border: 0px;\n"
"}")
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(Form)
        self.lastname.setGeometry(QtCore.QRect(510, 261, 191, 25))
        self.lastname.setStyleSheet("#lastname{\n"
"border: 0px;\n"
"}")
        self.lastname.setObjectName("lastname")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(510, 302, 191, 25))
        self.username.setStyleSheet("#username{\n"
"border: 0px;\n"
"}")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(510, 341, 191, 25))
        self.password.setStyleSheet("#password{\n"
"border: 0px;\n"
"}")
        self.password.setObjectName("password")
        self.pushButton_login = QtWidgets.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(50, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet("#pushButton_login{\n"
"color: white;\n"
"background-color: #0a9cad;\n"
"border: 1px white;\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_login.setFlat(False)
        self.pushButton_login.setObjectName("pushButton_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "[SSIS] Sign Up"))
        self.label_username.setText(_translate("Form", "Username:"))
        self.label_password.setText(_translate("Form", "Password:"))
        self.pushButton_signup.setText(_translate("Form", "Sign Up"))
        self.label_lastname.setText(_translate("Form", "Last Name:"))
        self.label_firstname.setText(_translate("Form", "First Name:"))
        self.pushButton_login.setText(_translate("Form", "Log In"))
