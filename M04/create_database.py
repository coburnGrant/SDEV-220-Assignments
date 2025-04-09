import sqlite3
import csv

# Create the database
sqlite_conn = sqlite3.connect('books.db')

cursor = sqlite_conn.cursor()

cursor.execute('DROP TABLE IF EXISTS books')

cursor.execute(
    '''
    CREATE TABLE books (
        title TEXT,
        author TEXT,
        year INTEGER               
    )
    '''
)

with open('books2.csv', newline='') as f:
    reader = csv.DictReader(f)
    rows = [(row['title'], row['author'], int(row['year'])) for row in reader]
    cursor.executemany('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', rows)

sqlite_conn.commit()

sqlite_conn.close()