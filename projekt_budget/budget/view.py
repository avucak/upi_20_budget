from bottle import template

class CategoryView():

    @staticmethod
    def categoryShow(categories=[], validation="", validationEdit="", editId="", display="none"):
        return template('categories', data=categories, validation=validation, validationEdit=validationEdit, editId=editId, disp=display)

    @staticmethod
    def categoryAdd(categories=[], validation="", validationEdit="", editId="", display="none"):
        return template('categories', data=categories, validation=validation, validationEdit=validationEdit, editId=editId, disp=display)

class TransactionView():

    @staticmethod
    def transactionShow():
        return ""
    @staticmethod
    def transactionAdd(categories=[]):
        return template("add_transaction", categories=categories)
