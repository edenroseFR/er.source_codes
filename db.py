import mysql.connector as mysql

database = mysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = 'edenrose',
                                 database = 'student_information')
cursor = database.cursor()

def students(query = 'SELECT * FROM students'):
    cursor.execute(query)
    students = cursor.fetchall()
    students = [list(student) for student in students]

    for i in range(len(students)):
        if students[i][2] != '':
            students[i] = [students[i][0], students[i][1] + ' '+ students[i][2][0] + '. ' + students[i][3], students[i][4], students[i][5], students[i][6]]
        else:
            students[i] = [students[i][0], students[i][1] + ' '+ students[i][2] + ' ' + students[i][3], students[i][4], students[i][5], students[i][6]]

    return students

def get_student(id=None):
    query = 'SELECT * FROM students where students_id = "%s"' % id
    cursor.execute(query)
    result = cursor.fetchall()
    result = list(result[0])

    return result

def get_IDs():
    query = ('SELECT students_id FROM students')
    cursor.execute(query)
    ids = cursor.fetchall()
    ids = [list(id) for id in ids]

    for i in range(len(ids)):
        ids[i]  = ids[i][0]

    return ids


def get_lastname(last_name = None):
    query = ('SELECT * FROM students where last_name = "%s"' % last_name)
    cursor.execute(query)
    lastnames = cursor.fetchall()
    students = [list(lastname) for lastname in lastnames]

    for i in range(len(students)):
        if students[i][2] != '':
            students[i] = [students[i][0], students[i][1] + ' '+ students[i][2][0] + '. ' + students[i][3], students[i][4], students[i][5], students[i][6]]
        else:
            students[i] = [students[i][0], students[i][1] + ' '+ students[i][2] + ' ' + students[i][3], students[i][4], students[i][5], students[i][6]]

    return students


def get_StudentLastname(query='SELECT last_name FROM students'):
    cursor.execute(query)
    lastnames = cursor.fetchall()
    lastnames = [list(lastname) for lastname in lastnames]
    unique_ln = []

    for i in range(len(lastnames)):
        lastnames[i] = lastnames[i][0]

    for i in lastnames:
        if i not in unique_ln:
            unique_ln.append(i)

    return unique_ln




def get_courses(query='SELECT course_code from courses'):
    cursor.execute(query)
    courses = cursor.fetchall()
    courses = [list(i) for i in courses]

    for i in range(len(courses)):
        courses[i] = courses[i][0]

    return courses


def add_course(course_code = None, course_name = None):
    query = ('INSERT into courses (course_code, course_name) VALUES("%s", "%s");' % (course_code, course_name))
    cursor.execute(query)
    database.commit()
    return


def update_student(id, first, middle, last, course, year, gender):
    query = ('UPDATE students SET first_name = "%s", middle_name = "%s", last_name = "%s", fk_course_code = "%s", year_level = "%s", gender = "%s" WHERE students_id = "%s";' % ( first, middle, last, course, year, gender, id ))
    cursor.execute(query)
    database.commit()

    return


def delete_student(id):
    query = ('DELETE FROM students WHERE students_id  = "%s";' % id)
    cursor.execute(query)
    database.commit()
    return

def add_student(id, first, middle, last, course, year, gender):
    query = ('INSERT INTO students(students_id, first_name, middle_name, last_name, fk_course_code, year_level, gender) VALUES("%s", "%s","%s","%s","%s","%s","%s")'%(id,first,middle,last,course,year,gender))
    cursor.execute(query)
    database.commit()
    return

