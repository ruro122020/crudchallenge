from __init__ import CONN, CURSOR  
import ipdb
from library import Library
from book import Book

Library.drop_table()
Library.create_table()

Book.drop_table()
Book.create_table()

nooks = Library.create('Nooks')
fisk = Library.create('Fisk')
google = Library.create('Google')

Book.create('Remember Me', 'Christopher Pike', 1980, nooks.id)
Book.create('IT', 'Stephen King', 1970, nooks.id)
Book.create("World War II", "Eve Sanders", 2000, fisk.id)

libraries = CURSOR.execute("""SELECT * FROM libraries""").fetchall()
books = CURSOR.execute("""SELECT * FROM  books""").fetchall()
print(libraries)
print(books)
# ipdb.set_trace()
