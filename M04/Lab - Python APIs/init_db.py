from app import app, db, Book
import csv

def load_books_from_csv():
    with open('books.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            book = Book(
                book_name=row['name'],
                author=row['author'],
                publisher=row['publisher']
            )
            db.session.add(book)
    db.session.commit()

with app.app_context():
    # Create all tables
    db.create_all()
    
    # Delete existing data
    Book.query.delete()
    
    # Load books from CSV
    load_books_from_csv()
    
    print("Database tables created and populated with books successfully!")
    