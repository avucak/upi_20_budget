if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath("../budget"))

import unittest, model_category, model_transaction, sqlite3

class TestTransactionModel(unittest.TestCase):
    def setUp(self):
        self.dbTrans = model_transaction.TransactionModelSQLite("unit_database.db")
        self.dbCat = model_category.CategoryModelSQLite("unit_database.db")

    def tearDown(self):
        del(self.dbTrans)
        del(self.dbCat)
        os.remove("unit_database.db")

    def insert_categories(self):
        self.dbCat.category_insert("Bills")
        self.dbCat.category_insert("Rent")
        self.dbCat.category_insert("Food")
        

##    def test_transaction_select_empty(self):
##        self.assertCountEqual(self.dbTrans.transaction_select(), [])
##
##    def test_transaction_select_3(self):
##        self.insert_categories()
##
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-05")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                  (2, "Dinner", 3, 35.45, "2019-12-05", ""),
##                                                                  (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##
##    def test_transaction_select_by_date(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        
##        self.assertCountEqual(self.dbTrans.transaction_select(date="2019-12-10"), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                  (2, "Dinner", 3, 35.45, "2019-12-10", "")])
##
##    def test_transaction_select_by_category(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        self.dbTrans.transaction_insert("Lunch", 3, 26.75, "2019-12-20", "Lunch with friends")
##        
##        self.assertCountEqual(self.dbTrans.transaction_select(category="3"), [(2, "Dinner", 3, 35.45, "2019-12-10", ""),
##                                                                              (4, "Lunch", 3, 26.75, "2019-12-20", "Lunch with friends")])
##
##    def test_transaction_select_by_category_and_date(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        self.dbTrans.transaction_insert("Lunch", 3, 26.75, "2019-12-20", "Lunch with friends")
##        
##        self.assertCountEqual(self.dbTrans.transaction_select(category="3", date="2019-12-20"), [(4, "Lunch", 3, 26.75, "2019-12-20", "Lunch with friends")])
##
##    def test_transaction_2_inserts_1_wrong(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Dinner",3, 79.99, "2019-12-10", "moja napomena")
##        with self.assertRaises(model_transaction.IntegrityError):
##            self.dbTrans.transaction_insert("Water bill",10, 150, "2019-12-05")
##        self.dbTrans.transaction_insert("Electricity bill",1, 79.99, "2019-12-30", "December")
##            
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Dinner",3, 79.99, "2019-12-10", "moja napomena"),
##                                                                  (2, "Electricity bill",1, 79.99, "2019-12-30", "December")])
##        
##    def test_transaction_3_inserts_1_delete(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        self.dbTrans.transaction_delete(2)
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                              (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##
##    def test_transaction_3_inserts_1_update_name(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        self.dbTrans.transaction_update(2, "Lunch", 3, 35.45, "2019-12-10")
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                  (2, "Lunch", 3, 35.45, "2019-12-10", ""),
##                                                                  (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##
##    def test_transaction_3_inserts_1_update_note_and_name(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        self.dbTrans.transaction_update(2, "Lunch", 3, 35.45, "2019-12-10", "Went out with colleagues after work")
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                  (2, "Lunch", 3, 35.45, "2019-12-10", "Went out with colleagues after work"),
##                                                                  (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##
##    def test_transaction_3_inserts_1_wrong_update(self):
##
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
##        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
##        with self.assertRaises(model_transaction.IntegrityError):
##            self.dbTrans.transaction_update(4, "Lunch", 3, 35.45, "2019-12-10")
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                  (2, "Dinner", 3, 35.45, "2019-12-10", ""),
##                                                                  (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##
##    def test_transaction_insert_wrong_amount(self):
##        self.insert_categories()
##        
##        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
##        with self.assertRaises(model_transaction.IntegrityError):
##            self.dbTrans.transaction_insert( "Lunch", 3, "abc", "2019-12-10")
##
##        self.assertCountEqual(self.dbTrans.transaction_select(), [(1, "Water bill", 1, 79.99, "2019-12-10", "November")])

    def test_transaction_sort_by_amount_desc(self):
        self.insert_categories()
        
        self.dbTrans.transaction_insert("Water bill", 1, 79.99, "2019-12-10", "November")
        self.dbTrans.transaction_insert("Dinner", 3, 35.45, "2019-12-10")
        self.dbTrans.transaction_insert("Rent", 2, 150, "2019-12-01", "Rent for November")
        for t in self.dbTrans.transaction_sort(amount=True, desc=True):
            print(t)

        self.assertCountEqual(self.dbTrans.transaction_sort(amount=True, desc=True), [(1, "Water bill", 1, 79.99, "2019-12-10", "November"),
                                                                  (2, "Dinner", 3, 35.45,"2019-12-10", ""),
                                                                  (3, "Rent", 2, 150, "2019-12-01", "Rent for November")])
##        self.assertCountEqual(self.dbTrans.transaction_sort(amount=True, desc=True), [(3, "Rent", 2, 80, "2019-12-01", "Rent for November"),
##                                                                                      (1, "Water bill", 1, 79.99, "2019-12-10", "November"),
##                                                                                      (2, "Dinner", 3, 35.45, "2019-12-10", "")])
        
        
        
if __name__ == "__main__":
    unittest.main()
