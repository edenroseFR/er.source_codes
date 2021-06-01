from PyQt5 import QtCore, QtGui, QtWidgets
from ssis_form_UI import *
import sys
import db

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initializeUI()

    def initializeUI(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.setText('Click Me')
        self.button.clicked.connect(self.pressed)

        self.show()
    def pressed(self):
        a = NewWin(self)
        a.show()
    def passed(self, nt):
        self.button.setText(nt)


class NewWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(NewWin, self).__init__(parent)
        self.p = parent
        self.initializeUI()
    def initializeUI(self):
        self.newbutton = QtWidgets.QPushButton(self)
        self.newbutton.setText('NewWin Button')
        self.newbutton.clicked.connect(self.d)
        self.show()
    def d(self):
        self.p.passed('k')
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

main()

