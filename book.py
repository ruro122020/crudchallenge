from __init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(self, title, author, published_year, library_id):
        self.id = None
        self.title = title
        self.author = author
        self.published_year = published_year
        self.library_id = library_id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError('title must be of type string')
        
    @property
    def author(self):
        return self._author 
    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError('author must be of type string')
    
    @property
    def published_year(self):
        return self._published_year 
    @published_year.setter
    def published_year(self, published_year):
        if isinstance(published_year, int) and published_year:
            self._published_year = published_year
        else: 
            raise ValueError("published_year must be of type int")


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            published_year INTEGER,
            library_id INTEGER,
            FOREIGN KEY (library_id) REFERENCES libraries(id))
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, title, author, published_year, library_id):
        book = cls(title, author, published_year, library_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all[row[0]]
        if book:
            book.title = row[1]
            book.author = row[2]
            book.published_year = row[3]
            book.library_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT * FROM books
            WHERE title = ? 
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        sql ="""
            INSERT INTO books (title, author, published_year, library_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.published_year, self.library_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, published_year = ?, library_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.title, self.author, self.published_year, self.library_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    