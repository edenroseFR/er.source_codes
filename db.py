import mysql.connector as mysql

database = mysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = 'edenrose',
                                 database = 'student_information')
cursor = database.cursor()