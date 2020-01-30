from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view_category import CategoryView

from model_category import CategoryModelSQLite
from model_transaction import TransactionModelSQLite

filename = abspath(join(dirname(__file__), "..", "category.db"))

dbTrans=TransactionModelSQLite(filename)
dbCat=CategoryModelSQLite(filename)
uiCat=CategoryView()

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
            return uiCat.categoryShow(categories)
    elif action=="delete":
        categoryName = request.forms.categoryname
        # provjera postoje li transakcije s tom kategorijom
        categoryId = dbCat.category_select(categoryName)[0][0]
        transactions = dbTrans.transaction_select(category=categoryId)
        if transactions == []:
            dbCat.category_delete(request.forms.categoryname)
            categories=dbCat.category_select()
            return uiCat.categoryShow(categories)
        else:
            categories=dbCat.category_select()
            return uiCat.categoryShow(categories,deleteWarning=categoryId)
    elif action=="edit":
        editId=dbCat.category_select(request.forms.oldName)[0][0]
        validationEdit=category_validate(request.forms.nameEdit)
        if validationEdit:
            categories=dbCat.category_select()
            return uiCat.categoryShow(categories=categories, validationEdit=validationEdit, editId=editId)
        else:
            dbCat.category_update(request.forms.oldName, request.forms.nameEdit)
            categories=dbCat.category_select()
            return uiCat.categoryShow(categories)


