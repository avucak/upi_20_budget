from bottle import template
class TransactionView():

    @staticmethod
    def transactionShow(categories=[], transactions=[], catChecked=[], minA="", maxA="", minD="", maxD="", option="other", filtered=False, sort=False):
        return template('transactions', categories=categories, transactions=transactions, categoriesChecked=catChecked, minAmount=minA, maxAmount=maxA, minDate=minD, maxDate=maxD, option=option, filtered=filtered, sort=sort)

    @staticmethod
    def transactionDetails(transaction=[], category=""):
        return template('transaction_details', transaction=transaction, category=category)

    @staticmethod
    def transactionAdd(categories=[], disable="false"):
        return template("add_transaction", categories=categories, disable=disable)

    @staticmethod
    def transactionAddValidate(categories=[], validation="", name="", category="", amount="", date="", note="", add="True"):
        return template("add_transaction_valid", categories=categories, validation=validation, name=name, category=category, amount=amount, date=date, note=note, add=add)

    @staticmethod
    def transactionEdit(categories=[], validation="", transId="", name="", category="", amount="", date="", note=""):
        return template("edit_transaction", categories=categories, transId=transId, validation=validation, name=name, category=category, amount=amount, date=date, note=note)
