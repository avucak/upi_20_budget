from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view import TransactionView

from model_category import CategoryModelSQLite
from model_transaction import TransactionModelSQLite

from datetime import datetime
import calendar

filename = abspath(join(dirname(__file__), "..", "category.db"))

dbCat=CategoryModelSQLite(filename)

dbTrans=TransactionModelSQLite(filename)
uiTrans=TransactionView()


def transaction_validate(name=None, category=None, amount=None, date=None, note=None):
    valid = {}
    if name is not None:
        if name.strip()=="":
            valid["name"] = "Transaction must have a name"
    if category is None:
        valid["category"] = "Transaction must have a category"
    if amount is not None:
        if amount.strip()=="":
            valid["amount"] = "Transaction must have an amount"
        else:
            try:
                float(amount)
            except ValueError:
                valid["amount"] = "Amount must be a real number"
    if date is not None:
        if date.strip()=="":
            valid["date"] = "Transaction must have a date"
        else:
            today = datetime.today().strftime('%Y-%m-%d')
            if date > today:
                valid["date"] = "Transaction date must be today or earlier"
    return valid


@route('/transactions')
def show_transactions():
    categories = dbCat.category_select()
    # ako radimo remove kod filtera, a informacije sortirane, trebamo proslijediti sort opciju
    option=request.query.optionSort
    if option=="":
        option="other"
    options=sortOptions(option)
    transactions = dbTrans.transaction_select(amountSort=options[0], dateSort=options[1], descSort=options[2])
    return uiTrans.transactionShow(categories=categories, transactions=transactions, option=option)

@route('/transactions/<transId>')
def showTransactionDetails(transId):
    transactions = dbTrans.transaction_select(transactionId=transId)
    categories = dbCat.category_select()
    for cat in categories:
        if cat[0]==transactions[0][2]:
            category=cat[1]
        
    return uiTrans.transactionDetails(transactions[0], category)

@route('/transactions/add')
def show_add_transaction():
    categories = dbCat.category_select()
    if categories == []:
        return uiTrans.transactionAdd(disable="true")
    return uiTrans.transactionAdd(categories=categories)

@post('/transactions/add')
def add_transaction():
    name = request.forms.transactionName
    category = request.forms.transactionCategory
    amount = request.forms.transactionAmount
    date = request.forms.transactionDate
    note = request.forms.transactionNote

    validation = transaction_validate(name,category,amount,date,note)
    categories=dbCat.category_select()
    if validation:
        return uiTrans.transactionAddValidate(categories,validation,name,category,amount,date,note,add="True")
    else:
        categoryId = dbCat.category_select(category)[0][0]
        dbTrans.transaction_insert(name,categoryId,amount,date,note)
        redirect("/transactions")

@route('/transactions/edit/<transactionId>')
def show_edit_transaction(transactionId):
    transaction = dbTrans.transaction_select(transactionId=transactionId)[0]
    name = transaction[1]
    category = transaction[2]
    amount = transaction[3]
    date = transaction[4]
    note = transaction[5]

    categories = dbCat.category_select()
    return uiTrans.transactionEdit(categories=categories,validation={}, transId=transactionId, name=name,category=category,amount=amount,date=date,note=note)

@post('/transactions/edit/<transactionId>')
def edit_transaction(transactionId):
    name = request.forms.transactionName
    category = request.forms.transactionCategory
    amount = request.forms.transactionAmount
    date = request.forms.transactionDate
    note = request.forms.transactionNote

    validation = transaction_validate(name,category,amount,date,note)
    categories = dbCat.category_select()
    if validation:
        return uiTrans.transactionAddValidate(categories,validation,name,category,amount,date,note,add="False")
    else:
        categoryId = dbCat.category_select(category)[0][0]
        dbTrans.transaction_update(transactionId,name,categoryId,amount,date,note)
        redirect("/transactions")

@post('/transactions')
def transaction_action():
    action = request.forms.action
    if action == "delete":
        dbTrans.transaction_delete(request.forms.transactionId)
        redirect("/transactions")

    if action == "sortFilter":
        categories = dbCat.category_select()
        buttonClicked = request.forms.actionButton
        previouslyFiltered = request.forms.filtered == "True"
        previouslySorted = request.forms.sorted == "True"
        # filter information
        checkedCategories = []
        checkboxCategories = [1]
        minAmount, maxAmount, minDate, maxDate= None, None, None, None
        if request.forms.minAmount:
            minAmount = request.forms.minAmount
        if request.forms.maxAmount:
            maxAmount = request.forms.maxAmount
        if request.forms.minDate:
            minDate = request.forms.minDate
        if request.forms.maxDate:
            maxDate = request.forms.maxDate
        if request.forms.checkboxAll:
            for cat in categories:
                checkedCategories.append(cat[0])
                checkboxCategories.append(1)
        else:
            checkboxCategories[0]=0
            for cat in categories:
                categoryName = str(cat[1])
                if request.forms.get(categoryName):
                    checkedCategories.append(cat[0])
                    checkboxCategories.append(1)
                else:
                    checkboxCategories.append(0)
        # sort information
        option = request.forms.sortOption
        if option=="":
            option="other"
        options=sortOptions(option)
        if buttonClicked=="Apply": #filter
            filtered = True
            sort = previouslySorted
            if previouslySorted:
                transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate, amountSort=options[0], dateSort=options[1], descSort=options[2])
            else:
                transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate)
        else: # sort
            filtered = previouslyFiltered
            sort = True
            if previouslyFiltered:
                transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate, amountSort=options[0], dateSort=options[1], descSort=options[2])
            else:
                transactions = dbTrans.transaction_select(amountSort=options[0], dateSort=options[1], descSort=options[2])
        return uiTrans.transactionShow(categories=categories, transactions=transactions, catChecked=checkboxCategories, minA=minAmount, maxA=maxAmount, minD=minDate, maxD=maxDate, option=option, filtered=filtered, sort=sort)


def sortOptions(option):
    options=[None, None, None] #amountSort, dateSort, descSort
    if option=="lowest":
        options[0] = True
    elif option=="highest":
        options[0] = True
        options[2] = True
    elif option=="oldest":
        options[1] = True
    elif option=="newest":
        options[1] = True
        options[2] = True
    return options

