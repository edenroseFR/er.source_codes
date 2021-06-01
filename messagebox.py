from PyQt5.QtWidgets import QMessageBox

def noResult(parent=None):
    QMessageBox.information(parent, 'Search Result',  'No student found!')

