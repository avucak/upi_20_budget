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
    def transactionShow(transactions=[], option="other"):
        return template('transactions', transactions=transactions, option=option)
    
    @staticmethod
    def transactionAdd(categories=[], disable="false"):
        return template("add_transaction", categories=categories, disable=disable)

    @staticmethod
    def transactionAddValidate(categories=[], validation="", name="", category="", amount="", date="", note="", add="True"):
        return template("add_transaction_valid", categories=categories, validation=validation, name=name, category=category, amount=amount, date=date, note=note, add=add)

    @staticmethod
    def transactionEdit(categories=[], validation="", name="", category="", amount="", date="", note=""):
        return template("edit_transaction", categories=categories, validation=validation, name=name, category=category, amount=amount, date=date, note=note)


