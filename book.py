from __init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(self, title, author, published_year, library_id):
        self.id = None
        self.title = title
        self.author = author
        self.published_year = published_year
        self.library_id = library_id

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