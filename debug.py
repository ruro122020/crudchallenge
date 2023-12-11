from __init__ import CONN, CURSOR  
import ipdb
from library import Library


Library.drop_table()
Library.create_table()

nooks = Library.create('Nooks')
fisk = Library.create('Fisk')
google = Library.create('Google')

nooks.name = 'Brooks'
nooks.update()

CURSOR.execute("""SELECT * FROM libraries""")
libraries = CURSOR.fetchall()
print(libraries)
# ipdb.set_trace()
