from __init__ import CURSOR, CONN

class Book:
    def __init__(self, title, author, published_year):
        self.id = None
        self.title = title
        self.author = author
        published_year = published_year  

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INT PRIMARY KEY,
            title TEXT,
            author TEXT,
            published_year INT,
            library_id INT,
            FOREIGN KEY(library_id) REFERENCES libraries(id))
        """
        CURSOR.execute(sql)
        CONN.commit()


class Library:

    books = [] #store multiple books

    def __init__(self, name):
        self.name = name
    
    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS libraries (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    def add_book(self, book):
        #adds a book to the library
        sql = """
        """
        pass
    def display_books(self):
        #Display information about all the books in the library
        pass
    
    def find_books_by_author(self, author):
        #finds and displays books by a specific author
        pass
    def remove_book(self, title):
        # Removes a book from the library by title
        pass


