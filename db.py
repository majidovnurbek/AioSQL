import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('preson.db')
cursor = conn.cursor()

# Define the users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(255),
        username VARCHAR(255),
        user_id INTEGER
    )
''')
conn.commit()



class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, full_name, username, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (full_name, username, user_id) VALUES (?, ?, ?)',
                                       (full_name, username, user_id))
