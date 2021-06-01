from PyQt5.QtWidgets import QMessageBox

def noResult(parent=None):
    QMessageBox.information(parent, 'Search Result',  'No student found!')

def confirmDelete(parent=None, name=None):
    prompt = QMessageBox.warning(parent, 'Confirm Deletion', 'This action cannot be undone.\nAre you sure you want to delete %s ?' % name, QMessageBox.Ok, QMessageBox.Cancel)
    if prompt == QMessageBox.Ok:
        return 'continue'
    else:
        return 'cancel'

def addSuccessful(parent=None):
    QMessageBox.information(parent, 'Student Added', 'Student added Successfully!')