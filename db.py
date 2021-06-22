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

def courses(query='SELECT course_code, course_name, COUNT(*) AS num from courses c '\
                        'JOIN students s ON c.course_code=s.fk_course_code '\
                        'GROUP BY c.course_code'):
    cursor.execute(query)
    courses = cursor.fetchall()
    courses = [list(i) for i in courses]
    existing = [i[0] for i in courses]

    query2 = 'SELECT course_code, course_name, 0 as num from courses'
    cursor.execute(query2)
    coursesWithNoStudents = cursor.fetchall()
    coursesWithNoStudents = [list(i) for i in coursesWithNoStudents]

    for i in coursesWithNoStudents:
        if i[0] not in existing:
            courses.append(i)

    return courses

def search_course(query = None):
    cursor.execute(query)
    courses = cursor.fetchall()
    courses = [list(i) for i in courses]

    return courses


def delete_course(course_code = None):
    query = ('DELETE FROM courses WHERE course_code = "%s"' % course_code)
    cursor.execute(query)
    database.commit()
    return


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


def get_student_with_lastname(last_name = None):
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

def get_StudentLevel(query='SELECT year_level FROM students'):
    cursor.execute(query)
    levels = cursor.fetchall()
    levels = [list(level) for level in levels]
    unique_yl = []

    for i in range(len(levels)):
        levels[i] = levels[i][0]

    for i in levels:
        if i not in unique_yl:
            unique_yl.append(i)

    return unique_yl


def get_StudentCourse(query='SELECT fk_course_code FROM students'):
    cursor.execute(query)
    courses = cursor.fetchall()
    courses = [list(course) for course in courses]
    unique_c = []

    for i in range(len(courses)):
        courses[i] = courses[i][0]

    for i in courses:
        if i not in unique_c:
            unique_c.append(i)

    return unique_c

def get_student_with_course(ccode=None):
    query = ('SELECT * FROM students where fk_course_code = "%s"' % ccode)
    cursor.execute(query)
    courses = cursor.fetchall()
    students = [list(course) for course in courses]

    for i in range(len(students)):
        if students[i][2] != '':
            students[i] = [students[i][0], students[i][1] + ' ' + students[i][2][0] + '. ' + students[i][3],
                           students[i][4], students[i][5], students[i][6]]
        else:
            students[i] = [students[i][0], students[i][1] + ' ' + students[i][2] + ' ' + students[i][3], students[i][4],
                           students[i][5], students[i][6]]

    return students

def get_student_with_year(yearLevel = None):
    query = ('SELECT * FROM students where year_level = "%s"' % str(yearLevel))
    cursor.execute(query)
    yearlevels = cursor.fetchall()
    students = [list(yearlevel) for yearlevel in yearlevels]

    for i in range(len(students)):
        if students[i][2] != '':
            students[i] = [students[i][0], students[i][1] + ' ' + students[i][2][0] + '. ' + students[i][3],
                           students[i][4], students[i][5], students[i][6]]
        else:
            students[i] = [students[i][0], students[i][1] + ' ' + students[i][2] + ' ' + students[i][3], students[i][4],
                           students[i][5], students[i][6]]

    return students


def get_courses(query='SELECT course_code from courses'):
    cursor.execute(query)
    courses = cursor.fetchall()
    courses = [list(i) for i in courses]

    for i in range(len(courses)):
        courses[i] = courses[i][0]

    return courses

def get_courseName(code=None):
    query = 'SELECT course_name from courses WHERE course_code = "%s"' % code
    cursor.execute(query)
    result = cursor.fetchall()
    result = list(result[0])
    result = result[0]

    return result

def update_course(course_code = None, course_name = None):
    query = ('UPDATE courses SET course_name = "%s" WHERE course_code = "%s"' % (course_name, course_code))
    cursor.execute(query)
    database.commit()
    return


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
