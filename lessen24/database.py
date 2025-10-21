import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Recreate the table with the correct schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

connection.commit()

# Insert data
cursor.executemany('''
INSERT INTO employees (name, position, department, salary)
VALUES (?, ?, ?, ?)
''', [
    ('John Doe', 'Software Engineer', 'IT', 75000.00),
    ('Jane Smith', 'Data Analyst', 'Marketing', 65000.00),
    ('Emily Johnson', 'Project Manager', 'Operations', 85000.00),
])

connection.commit()

# Fetch and print data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()