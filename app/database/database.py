import sqlite3

connection = sqlite3.connect(
    'mood_history.db'
)

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS moods(
id INTEGER PRIMARY KEY,
emotion TEXT,
created TEXT
)
''')

connection.commit()