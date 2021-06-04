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

def wrongPattern(parent=None):
    QMessageBox.information(parent, 'Invalid ID', 'Please follow the YYYY-NNNN pattern for the ID.\nExample: 2019-2143')

def incompleteInfo(parent=None):
    QMessageBox.information(parent, 'Incomplete Information', 'Please fill all the fields provided.')

def idAlreadyTaken(parent=None, studID=None):
    QMessageBox.information(parent, 'Duplicate ID', '%s is already in used. Please use a unique ID.' % studID)

def confirmAddCourse(parent=None, ccode=None, cname=None):
    prompt = QMessageBox.question(parent, 'Confirm Add', 'Are you sure you want to add %s as %s ?' %(ccode, cname))
    if prompt == QMessageBox.Yes:
        return 'continue'
    else:
        return 'cancel'

def addCoursePrompt(parent=None):
    prompt = QMessageBox.question(parent, 'New Course Detected', 'New Course detected.\nDo you want this to be added in in your course list?')
    if prompt == QMessageBox.Yes:
        return 'continue'
    else:
        return 'cancel'

def courseAdded(parent=None):
    QMessageBox.information(parent, 'Add Successful', 'New course added successfully!')


def cantDeleteCourse(parent=None, name=None, enrolled=None):
    prompt = QMessageBox.warning(parent, 'Deletion Error.',
                                 '%s cannot be deleted\nbecause %s students are enrolled in this course.' % (name, str(enrolled)),
                                 QMessageBox.Ok, QMessageBox.Ok)
