from __init__ import CONN, CURSOR  
from book_library import Book
from book_library import Library
import random
import ipdb



nooks_library = Library("Nooks")
nooks_library.create_table()
Book.create_table()


ipdb.set_trace()
