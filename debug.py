###MAPPING PYTHON CLASSES TO DATABASE###

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

remember_me = Book.create('Remember Me', 'Christopher Pike', 1980, nooks.id)
it = Book.create('IT', 'Stephen King', 1970, nooks.id)
world_war_2 = Book.create("World War II", "Eve Sanders", 2000, fisk.id)

print('Book Class', Book.all[3].author)
world_war_2.author = 'Jeff Hernandez'
world_war_2.update()
print('Book Class', Book.all[3].author)

it.delete()
print(Book.all[2].title)
libraries = CURSOR.execute("""SELECT * FROM libraries""").fetchall()
books = CURSOR.execute("""SELECT * FROM  books""").fetchall()
print(libraries)
print(books)

# ipdb.set_trace()
