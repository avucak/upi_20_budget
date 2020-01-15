from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view import CategoryView, TransactionView

from model_category import CategoryModelSQLite
from model_transaction import TransactionModelSQLite

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
   # name=request.forms.get('cname')
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

@route('/transactions/add')
def add_transaction():
    categories=dbCat.category_select()
    return uiTrans.transactionAdd(categories)

    
        

