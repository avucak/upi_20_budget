from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view import CategoryView, TransactionView

from model_category import CategoryModelSQLite
from model_transaction import TransactionModelSQLite

from datetime import datetime

filename = abspath(join(dirname(__file__), "..", "category.db"))

dbCat=CategoryModelSQLite(filename)
uiCat=CategoryView()

dbTrans=TransactionModelSQLite(filename)
uiTrans=TransactionView()

@route('/categories')
def show_category():
    categories=dbCat.category_select()
    return uiCat.categoryShow(categories)

def category_validate(name=None):
    valid=""
    if name is not None:
        cat=dbCat.category_select(name)
        if cat:
            valid="Category already exists"
        elif name.strip()=="":
            valid="Category must have a name"
    return valid
        
        

@post('/categories')
def add_category():
    name=request.forms.cname
    action=request.forms.action
    if action=="add":
        validation=category_validate(name)
        categories=dbCat.category_select()
        if validation:
            return uiCat.categoryShow(categories=categories, validation=validation, display="block")
        else:
            dbCat.category_insert(name)
            categories=dbCat.category_select()
            return uiCat.categoryAdd(categories)
    elif action=="delete":
        dbCat.category_delete(request.forms.categoryname)
        categories=dbCat.category_select()
        return uiCat.categoryAdd(categories)
    elif action=="edit":
        editId=dbCat.category_select(request.forms.oldName)[0][0]
        validationEdit=category_validate(request.forms.nameEdit)
        if validationEdit:
            categories=dbCat.category_select()
            return uiCat.categoryShow(categories=categories, validationEdit=validationEdit, editId=editId)
        else:
            dbCat.category_update(request.forms.oldName, request.forms.nameEdit)
            categories=dbCat.category_select()
            return uiCat.categoryAdd(categories)

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
    transactions = dbTrans.transaction_select()
    return uiTrans.transactionShow(categories=categories, transactions=transactions)


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
        transactions = dbTrans.transaction_select()
        categories = dbCat.category_select()
        return uiTrans.transactionShow(categories=categories, transactions=transactions)

@route('/transactions/edit/<transactionId>')
def show_edit_transaction(transactionId):
    transaction = dbTrans.transaction_select(transactionId=transactionId)[0]
    name = transaction[1]
    category = transaction[2]
    amount = transaction[3]
    date = transaction[4]
    note = transaction[5]
    
    categories = dbCat.category_select()
    return uiTrans.transactionEdit(categories=categories,validation={},name=name,category=category,amount=amount,date=date,note=note)

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
        transactions = dbTrans.transaction_select()
        categories = dbCat.category_select()
        return uiTrans.transactionShow(categories=categories, transactions=transactions)
        
@post('/transactions')
def transaction_action():
    categories = dbCat.category_select()
    action = request.forms.action
    if action == "delete":
        dbTrans.transaction_delete(request.forms.transactionId)
        transactions = dbTrans.transaction_select()
        return uiTrans.transactionShow(categories=categories, transactions=transactions)
    
    if action == "sortFilter":
        checkedCategories = []
        checkboxCategories = [1]
        buttonClicked= request.forms.actionButton
        #if buttonClicked=="Apply":
         #   return "A"
        #else:
         #   return "B"
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
                    
        option = request.forms.sortOption
        if option=="":
            option="other"
        transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate)
        #return uiTrans.transactionShow(categories=categories, transactions=transactions, catChecked=checkboxCategories, minA=minAmount, maxA=maxAmount, minD=minDate, maxD=maxDate, option=option)
    

        # sort
        
        if option=="lowest":
            transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate)
        elif option=="highest":
            transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate, amountSort=True, descSort=True)
        elif option=="oldest":
            transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate, dateSort=True)
        elif option=="newest":
            transactions = dbTrans.transaction_select(categories=checkedCategories, minAmount=minAmount, maxAmount=maxAmount, minDate=minDate, maxDate=maxDate, dateSort=True, descSort=True)

        return uiTrans.transactionShow(categories=categories, transactions=transactions, catChecked=checkboxCategories, minA=minAmount, maxA=maxAmount, minD=minDate, maxD=maxDate, option=option)
    
##    if action=="sort":
##            
##        option = request.forms.sortOption
##        if option=="lowest":
##            transactions = dbTrans.transaction_sort(amount=True)
##        elif option=="highest":
##            transactions = dbTrans.transaction_sort(amount=True, desc=True)
##        elif option=="oldest":
##            transactions = dbTrans.transaction_sort(date=True)
##        elif option=="newest":
##            transactions = dbTrans.transaction_sort(date=True, desc=True)
##        elif option=="other":
##            redirect("/transactions")
##    
##    return uiTrans.transactionShow(transactions=transactions, categories=categories, option=option)
    
                


    
