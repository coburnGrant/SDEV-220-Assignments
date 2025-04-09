from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __init__(self, json):
        self.book_name = json['book_name']
        self.author = json['author']
        self.publisher = json['publisher']

    def __repr__(self):
        return f'{self.book_name} - {self.author} - {self.publisher}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author': self.author,
            'publisher': self.publisher
        }

@app.route('/')
def index():
    return '''
    <h1>Welcome to a Book API!</h1>
    <h3>To get all books, go to <a href="/books">/books</a></h3>
    <h3>To get a specific book, go to /books/<id></h3>
    <h3>To add a book, POST to /books and use JSON payload</h3>
    <h3>To delete a book, DELETE to /books/<id></h3>
    '''

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append(book.to_dict())
    
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return book.to_dict()

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(json=request.json)

    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book is None:
        return {'message': 'Book not found'}, 404
    
    db.session.delete(book)
    db.session.commit()
    return {'message': 'Book deleted'}