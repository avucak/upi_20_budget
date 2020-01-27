from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view import CategoryView, TransactionView

from model_category import CategoryModelSQLite
from model_transaction import TransactionModelSQLite

from datetime import datetime
import calendar

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
    # ako radimo remove kod filtera, a informacije sortirane, trebamo proslijediti sort opciju
    option=request.query.optionSort
    if option=="":
        option="other"
    options=sortOptions(option)
    transactions = dbTrans.transaction_select(amountSort=options[0], dateSort=options[1], descSort=options[2])
    return uiTrans.transactionShow(categories=categories, transactions=transactions, option=option)


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

@route('/overview')
def overview_options():  
    categories = dbCat.category_select()
    today = datetime.today().strftime('%Y-%m-%d')
    daysInCurrentMonth = calendar.monthrange(int(today[:4]),int(today[5:7]))[1]
    firstDayCurrentMonth = datetime.today().replace(day=1).strftime('%Y-%m-%d')
    lastDayCurrentMonth = datetime.today().replace(day=daysInCurrentMonth).strftime('%Y-%m-%d')    
    return uiTrans.overviewOptions(categories=categories, minD=firstDayCurrentMonth, maxD=lastDayCurrentMonth)

def calculateSumAverage(totalSum, totalAverage, checkedCategories, transactions):
    for cat in checkedCategories:
        for t in transactions:
            if t[2]==cat[0]:
                totalSum[cat[0]-1]+=abs(t[3])

    for i in range(len(totalAverage)):
        totalAverage[i]=totalSum[i]/sum(totalSum)


@post('/overview/report')
def overview_report():
    categories = dbCat.category_select()
    checkedCategories=[]
    for cat in categories:
        if request.forms.get(cat[1]):
            c=[cat[0], cat[1]]
            checkedCategories.append(c)
            
    totalSum=[0 for c in categories]
    totalAverage=[0 for c in categories]

    minDate=request.forms.minDate
    maxDate=request.forms.maxDate
    transactions = dbTrans.transaction_select(minDate=minDate, maxDate=maxDate)

    calculateSumAverage(totalSum, totalAverage, checkedCategories, transactions)

    txt="------------------------------------------------------------------------\n"
    txt+="From "+minDate + " to "+maxDate+"\n------------------------------------------------------------------------\n\n"
    for cat in checkedCategories:
        txt+="--- "+ cat[1] + " ---\n"
        for t in transactions:
            if t[2]==cat[0]:
                txt+=t[1]+"   "+cat[1]+"   "+str(t[3])+"   "+t[4]+"   "+t[5]+"\n"
        txt+="Category total: "+str(totalSum[cat[0]-1])+"   Percentage: " + '%.2f' % (totalAverage[cat[0]-1]*100)+"%\n"
        txt+="------------------------------------------------------------------------\n\n"
    
    # spremanje u datoteku
    fileName="budget_report.txt"
    f= open(fileName,"w+")
    f.write(txt)
    f.close()

    return uiTrans.overviewReport(categories=categories, minD=minDate, maxD=maxDate, checkedCategories=checkedCategories, fileName=fileName)

@post('/overview/show')
def show_overview():
    categories = dbCat.category_select()
    transactions = dbTrans.transaction_select()
    checkedCategories=[]
    for cat in categories:
        if request.forms.get(cat[1]):
            c=[cat[0], cat[1]]
            checkedCategories.append(c)
            
    if checkedCategories==[]:
        return uiTrans.overviewShow(categories=categories, transactions=transactions)

        
    totalSum=[0 for c in categories]
    totalAverage=[0 for c in categories]
    calculateSumAverage(totalSum, totalAverage, checkedCategories, transactions)
    
    minDate=request.forms.minDate
    maxDate=request.forms.maxDate
    transactions = dbTrans.transaction_select(minDate=minDate, maxDate=maxDate)

    pieChartData=[]
    for cat in checkedCategories:
        pieChartData.append([cat[0], float('%0.2f' % (totalAverage[cat[0]-1]*100))])
    return uiTrans.overviewShow(categories=categories, transactions=transactions, checkedCategories=checkedCategories, totalSum=totalSum, totalAverage=totalAverage, pieChartData=pieChartData)


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

