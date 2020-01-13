import sqlite3
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath("../budget"))

import model_category


class IntegrityError(Exception):
    pass


class TransactionModelSQLite:
    
    def __init__(self, filename):
        self.conn = sqlite3.Connection(filename)
        self.cur = self.conn.cursor()

        self.cur.executescript("""
            CREATE TABLE IF NOT EXISTS transactions(
              id integer PRIMARY KEY,
              name text NOT NULL,
              category integer,
              amount real NOT NULL,
              date Date NOT NULL,
              note string,
              CONSTRAINT fk_category
              FOREIGN KEY (category)
              REFERENCES categories (id));""")

    def transaction_select(self, transactionId=None, name=None, category=None, amount=None, date=None):
        sql = "SELECT * FROM transactions "
        sql_where, sql_and = False, False
        cond = []
        for field, op, val in [("id", "=", transactionId), ("name", "=", name), ("amount", "=", amount), ("category", "=", category), ("date", "=", date)]:
            if val is not None:
                if not sql_where:
                    sql_where = True
                    sql += "WHERE "
                if sql_and:
                    sql += "AND "
                sql += "{} {} ? ".format(field, op)
                sql_and = True
                cond.append(val)

        self.cur.execute(sql, tuple(cond))
        return self.cur.fetchall()

    def transaction_insert(self, name, category, amount, date, note=""):
        try:
            self.cur.execute("""
                INSERT INTO transactions
                (name, category, amount, date, note)
                VALUES (?, ?, ?, ?, ?)""", (name, category, amount, date, note))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise IntegrityError("Greška!")
            
##            try:
##                float(amount)
##            except ValueError:
##                raise IntegrityError("Amount is not a number.")

    def transaction_update(self, transactionId, name, category, amount, date, note=""):
        if not self.student_select(transactionId=transactionId):
            raise IntegrityError("Transaction doesn't exist.")

        self.cur.execute("""
            UPDATE transactions
            SET name = ?, category = ?, amount = ?, date = ?, note = ?
            WHERE id = ?""", (name, category, amount, date, note, transactionId))
        self.conn.commit()

    def transaction_delete(self, transactionId):
        if not self.student_select(transactionId=transactionId):
            raise IntegrityError("Transaction doesn't exist.")

        self.cur.execute("""
            DELETE FROM transactions
            WHERE id = ?""", (transactionId, ))
        self.conn.commit()
            



class Transaction:

    def __init__(self, name, category, amount, date, note):
        self._name=name
        self._category=category
        self._amount=amount
        self._date=date
        self._note=note

    def __repr__(self):
        return "Transaction(" +self._name+", "+ self._category+", "+str(self._amount) +", "+self._date+")"


import unittest

class TestTransactionModel(unittest.TestCase):
    def setUp(self):
        self.db = TransactionModelSQLite("unit_database.db")
        self.dbCat = model_category.CategoryModelSQLite("unit_database.db")

    def tearDown(self):
        del(self.db)
        del(self.dbCat)
        os.remove("unit_database.db")

    def test_transaction_2_inserts(self):
        self.dbCat.category_insert("Bills")
        self.dbCat.category_insert("Rent")
        self.dbCat.category_insert("Food")
 
        self.db.transaction_insert("Water bill",1, 150, "2019-12-05")
        self.db.transaction_insert("Dinner",3, 79.99, "2019-12-10", "moja napomena")
        self.assertCountEqual(self.db.transaction_select(), [(1,"Water bill","Bills", 150, "2019-12-05",""), (2, "Dinner",3, 79.99, "2019-12-10", "moja napomena")])

if __name__ == "__main__":
    unittest.main()

    
