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
            new_name = name.capitalize()
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
    
    @classmethod
    def instance_from_db(cls, row):
        #check if row exist in dictionary
        library = cls.all[row[0]]

        if library:
          #make sure the value for that library matches
          library.name = row[1]
        else: 
            #if library instance doesn't exist in dictionary, create an instance and add it to the dictionary
            library = cls(row[1])
            library.id = row[0]
            cls.all[library.id] = library
        return library
            
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM libraries
        """
        rows = CURSOR.execute(sql).fetchall()
        CONN.commit()
        
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM libraries 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        new_name = name.capitalize()
        sql ="""
            SELECT * FROM libraries
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (new_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

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