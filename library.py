from __init__ import CONN, CURSOR

class Library:
    all = {}

    def __init__(self, name):
        self.id = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('name must be of type string')
    
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries(
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(self):
        sql = """
            DROP TABLE IF EXISTS libraries
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name):
        library = cls(name)
        library.save()
        return library

    def save(self):
        sql = """
            INSERT INTO libraries (name) VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE libraries
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM libraries 
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None