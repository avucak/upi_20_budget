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
        self.cur.execute("PRAGMA foreign_keys = ON")      
        self.cur.executescript("""
            CREATE TABLE IF NOT EXISTS transactions(
              id integer PRIMARY KEY,
              name text NOT NULL,
              category integer,
              amount real NOT NULL,
              date Date NOT NULL,
              note string,
              FOREIGN KEY(category) REFERENCES categories(id));""")

    def transaction_select(self, transactionId=None, name=None, category=None, categories=None, amount=None, minAmount=None, maxAmount=None, date=None, minDate=None, maxDate=None):
        sql = "SELECT * FROM transactions "
        sql_where, sql_and = False, False
        cond = []
        if categories is not None:
            if len(categories)>0:
                q = "("
                for cat in categories:
                    q += "?,"
                q = q[:-1]
                q += ")"
            else:
                categories = None
        for field, op, val in [("id", "=", transactionId), ("name", "=", name), ("amount", "=", amount), ("amount", ">=", minAmount), ("amount", "<=", maxAmount), ("category", "=", category), ("category", "IN", categories),("date", "=", date), ("date", ">=", minDate), ("date", "<=", maxDate)]:
            if val is not None:
                if not sql_where:
                    sql_where = True
                    sql += "WHERE "
                if sql_and:
                    sql += "AND "
                if val == categories:
                    sql += "{} {} {} ".format(field, op, q)
                    for cat in val:
                        cond.append(cat)
                else:
                    sql += "{} {} ? ".format(field, op)
                    cond.append(val)
                sql_and = True
                

        try:
            self.cur.execute(sql, tuple(cond))
            return self.cur.fetchall()
        except:
            ispis=""
            for c in cond:
                ispis+=c+" "
            raise Exception("Condition izgleda ovako: "+ispis+",a sam sql ovako:"+sql)

    def transaction_insert(self, name, category, amount, date, note=""):
        try:
            float(amount)
        except ValueError:
            raise IntegrityError("Amount is not a number.")
        try:
            self.cur.execute("""
                INSERT INTO transactions
                (name, category, amount, date, note)
                VALUES (?, ?, ?, ?, ?)""", (name, category, amount, date, note))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise IntegrityError("Greška!")
            


    def transaction_update(self, transactionId, name, category, amount, date, note=""):
        if not self.transaction_select(transactionId=transactionId):
            raise IntegrityError("Transaction doesn't exist.")

        self.cur.execute("""
            UPDATE transactions
            SET name = ?, category = ?, amount = ?, date = ?, note = ?
            WHERE id = ?""", (name, category, amount, date, note, transactionId))
        self.conn.commit()

    def transaction_delete(self, transactionId):
        if not self.transaction_select(transactionId=transactionId):
            raise IntegrityError("Transaction doesn't exist.")

        self.cur.execute("""
            DELETE FROM transactions
            WHERE id = ?""", (transactionId, ))
        self.conn.commit()

    def transaction_sort(self, category=None, amount=None, date=None, desc=False):    
        sql ="SELECT * FROM transactions ORDER BY "
        
        for field, val in [("amount", amount), ("category", category), ("date", date)]:
            if val is not None:
                sql+=field+" "            
        
        if desc:
            sql += "DESC"
        else:
            sql += "ASC"

        self.cur.execute(sql)
        return self.cur.fetchall()
            



class Transaction:

    def __init__(self, name, category, amount, date, note):
        self._name=name
        self._category=category
        self._amount=amount
        self._date=date
        self._note=note

    def __repr__(self):
        return "Transaction(" +self._name+", "+ self._category+", "+str(self._amount) +", "+self._date+")"



    
