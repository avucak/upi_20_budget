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
    def transactionShow(categories=[], transactions=[], catChecked=[], minA="", maxA="", minD="", maxD="", option="other", filtered=False, sort=False):
        return template('transactions', categories=categories, transactions=transactions, categoriesChecked=catChecked, minAmount=minA, maxAmount=maxA, minDate=minD, maxDate=maxD, option=option, filtered=filtered, sort=sort)

    @staticmethod
    def transactionAdd(categories=[], disable="false"):
        return template("add_transaction", categories=categories, disable=disable)

    @staticmethod
    def transactionAddValidate(categories=[], validation="", name="", category="", amount="", date="", note="", add="True"):
        return template("add_transaction_valid", categories=categories, validation=validation, name=name, category=category, amount=amount, date=date, note=note, add=add)

    @staticmethod
    def transactionEdit(categories=[], validation="", name="", category="", amount="", date="", note=""):
        return template("edit_transaction", categories=categories, validation=validation, name=name, category=category, amount=amount, date=date, note=note)

    @staticmethod
    def overviewOptions(categories=[], minD="", maxD=""):
        return template('overview_options', categories=categories, minDate=minD, maxDate=maxD)

    @staticmethod
    def overviewReport(categories=[], minD="", maxD="", fileName=""):
        return template('overview_report', categories=categories, minDate=minD, maxDate=maxD, fileName=fileName)

    

    @staticmethod
    def overviewShow(categories=[], transactions=[], checkedCategories=[], totalSum=[], totalAverage=[], pieChartData=[]):
        return template('overview', categories=categories, transactions=transactions, checkedCategories=checkedCategories, totalSum=totalSum, totalAverage=totalAverage, pieChartData=pieChartData)
