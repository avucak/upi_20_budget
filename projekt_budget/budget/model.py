import sqlite3
import os

class IntegrityError(Exception):
    pass

class CategoryModelSQLite:

    def __init__(self, filename):
        self.conn = sqlite3.Connection(filename)
        self.cur = self.conn.cursor()

        self.cur.executescript("""
            CREATE TABLE IF NOT EXISTS categories(
              id integer PRIMARY KEY,
              name text UNIQUE NOT NULL);""")


    def category_select(self, name=None):
        sql = "SELECT * FROM categories "
        cond=[]
        if name is not None:
            sql+="WHERE name = ? "
            cond.append(name)

        self.cur.execute(sql, tuple(cond))  
        return self.cur.fetchall()

    def category_insert(self, name):
        try:
            self.cur.execute("""
                INSERT INTO categories
                (name)
                VALUES (?)""", (name,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise IntegrityError("Category with that name already exists!")

    def category_update(self, name):
        if not self.category_select(name):
            raise IntegrityError("Category with that name doesn't exist.")

        self.cur.execute("""
            UPDATE categories
            SET name = ?
            WHERE id = ?""", (name, self.category_select(name)[0][0]))
        self.conn.commit()

    def student_delete(self, name):
        if not self.student_select(name):
            raise IntegrityError("Category with that name doesn't exist.")

        self.cur.execute("""
            DELETE FROM categories
            WHERE name = ?""", (name, ))
        self.conn.commit()


class Category:

    def __init__(self, name):
        self._name=name
        
    def __repr__(self):
        return "Category "+self._name
