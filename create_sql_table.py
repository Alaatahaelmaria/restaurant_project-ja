import sqlite3

# Create the database
conn = sqlite3.connect('users.db')

# Create users table
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert 5 initial users
users = [
    ('user1', 'pass1'),
    ('user2', 'pass2'),
    ('user3', 'pass3'),
    ('user4', 'pass4'),
    ('user5', 'pass5'),
]

conn.executemany("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", users)
conn.commit()
conn.close()

print("Database and initial users created successfully.")
