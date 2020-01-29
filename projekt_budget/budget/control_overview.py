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
        if sum(totalSum) != 0:
            totalAverage[i]=totalSum[i]/sum(totalSum)


@post('/overview/report')
def overview_report():
    categories = dbCat.category_select()
    checkedCategories=[]
    for cat in categories:
        if request.forms.get(cat[1]):
            c=[cat[0], cat[1]]
            checkedCategories.append(c)
    minDate, maxDate = None, None
    if request.forms.minDate:
        minDate=request.forms.minDate
    if request.forms.maxDate:
        maxDate=request.forms.maxDate
    transactions = dbTrans.transaction_select(minDate=minDate, maxDate=maxDate)
            
    totalSum=[0 for c in categories]
    totalAverage=[0 for c in categories]
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

    minDate, maxDate = None, None
    if request.forms.minDate:
        minDate=request.forms.minDate
    if request.forms.maxDate:
        maxDate=request.forms.maxDate
    transactions = dbTrans.transaction_select(minDate=minDate, maxDate=maxDate)
    
    totalSum=[0 for c in categories]
    totalAverage=[0 for c in categories]
    calculateSumAverage(totalSum, totalAverage, checkedCategories, transactions)
    

    pieChartData=[]
    for cat in checkedCategories:
        pieChartData.append([cat[0], float('%0.2f' % (totalAverage[cat[0]-1]*100))])
    return uiTrans.overviewShow(categories=categories, transactions=transactions, checkedCategories=checkedCategories, totalSum=totalSum, totalAverage=totalAverage, pieChartData=pieChartData)
