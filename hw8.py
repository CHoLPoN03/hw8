import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_countries(connection, countries):
    try:
        sql = '''
            INSERT INTO countries 
            (title)
            VALUES 
            (?)
        '''
        cursor = connection.cursor()
        cursor.executemany(sql, countries)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

sql_to_create_countries_table = ''' 
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
'''

my_connection = create_connection('countries.db')
if my_connection:
    print("Успешное подключение к базе данных")
    create_table(my_connection, sql_to_create_countries_table)
    # insert_countries(my_connection, [('Kyrgyzstan',), ('USA',), ('Japan',)])
    my_connection.close()

sql_to_create_cities_table = '''
CREATE TABLE IF NOT EXISTS cities (
    c_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area FLOAT DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
)'''

def insert_cities(connection, cities):
    try:
        sql = '''
            INSERT INTO cities 
            (title, area, country_id)
            VALUES 
            (?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.executemany(sql, cities)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

my_connection = create_connection('cities.db')
if my_connection:
    print("Успешное подключение к базе данных")
    create_table(my_connection, sql_to_create_cities_table)
    # insert_cities(my_connection, [('Bishkek', 20.9, 1), ('London', 1572.0, 2), ('Osaka', 220.5, 3), ('Tokio', 2187.66, 3), ('Bangok', 1568.7, 4), ('Pekin', 16410.54, 5), ('Dublin', 115, 6)])
    my_connection.close()

sql_to_create_students_table = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (c_id)
)'''

def insert_students(connection, students):
    try:
        sql = '''
            INSERT INTO students 
            (first_name, last_name, city_id)
            VALUES 
            (?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.executemany(sql, students)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


students_connection = create_connection('students.db')
if students_connection:
    print("Успешное подключение к базе данных")
    create_table(students_connection, sql_to_create_students_table)
    insert_students(students_connection, [('Иван', 'Иванов', 1), ('Петр', 'Петров', 1),
        ('Алексей', 'Алексеев', 2),
        ('Елена', 'Сидорова', 2),
        ('Анна', 'Иванова', 3),
        ('Дмитрий', 'Петров', 3),
        ('Мария', 'Сидорова', 4),
        ('Александр', 'Алексеев', 4),
        ('Светлана', 'Иванова', 5),
        ('Николай', 'Сидоров', 5),
        ('Ольга', 'Петрова', 6),
        ('Виктор', 'Александров', 6),
        ('Татьяна', 'Иванова', 7),
        ('Григорий', 'Петров', 7),
        ('Екатерина', 'Алексеева', 1) ])
    students_connection.close()


