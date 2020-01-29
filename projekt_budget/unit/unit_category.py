if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath("../budget"))
import unittest, model_category


class TestCategoryModel(unittest.TestCase):

    def setUp(self):
        self.db = model_category.CategoryModelSQLite("unit_category.db")

    def tearDown(self):
        del(self.db)
        os.remove("unit_category.db")

    def test_category_select_empty(self):
        self.assertCountEqual(self.db.category_select(), [])

    def test_category_select_3(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        self.db.category_insert("Food")
        self.assertCountEqual(self.db.category_select(), [(1, "Bills"), (2, "Rent"), (3, "Food")])

    def test_category_select_by_name(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        self.db.category_insert("Food")
        self.assertCountEqual(self.db.category_select(name="Rent"), [(2, "Rent")])

    def test_category_2_inserts_1_update(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        self.db.category_update("Rent", "Food")
        self.assertCountEqual(self.db.category_select(), [(1,"Bills"), (2, "Food")])

    def test_category_3_inserts_1_delete(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        self.db.category_insert("Food")
        self.db.category_delete("Rent")
        self.assertCountEqual(self.db.category_select(),[(1, "Bills"), (3, "Food")])

    def test_category_2_inserts_with_same_name(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        with self.assertRaises(model_category.IntegrityError):
            self.db.category_insert("Bills")
        self.assertCountEqual(self.db.category_select(), [(1, "Bills"), (2, "Rent")])

    def test_category_2_inserts_wrong_update(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        with self.assertRaises(model_category.IntegrityError):
            self.db.category_update("Rent","Bills")
        self.assertCountEqual(self.db.category_select(), [(1,"Bills"), (2, "Rent")])

    def test_category_2_inserts_wrong_delete(self):
        self.db.category_insert("Bills")
        self.db.category_insert("Rent")
        with self.assertRaises(model_category.IntegrityError):
            self.db.category_delete("Food")
        self.assertCountEqual(self.db.category_select(), [(1,"Bills"), (2, "Rent")])
        

if __name__ == "__main__":
    unittest.main()
