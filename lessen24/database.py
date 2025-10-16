import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
CREATE table if not exists employees (
    id integer primary key autoincrement,
    name text not null,
    position text not null,
    departament text not null,
    salary real 
)
''')
connection.commit()

cursor.execute('''
    isnert into employees (name, position, departament, salary)
    values (?, ?, ?, ?)
    '''        , ("John Doe", "Software Engineer", "IT", 75000))
connection.commit()

cursor.execute('SELECT * FROM employees')

