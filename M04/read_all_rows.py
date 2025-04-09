import sqlite3

with sqlite3.connect('books.db') as conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    
    print("All rows in books table:")
    for row in rows:
        print(row)