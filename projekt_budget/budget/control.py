from os.path import abspath, join, dirname
from bottle import route, run, post, request, redirect
from view import CategoryView

from model import CategoryModelSQLite

filename = abspath(join(dirname(__file__), "..", "category.db"))
db=CategoryModelSQLite(filename)
ui=CategoryView()


@route('/categories')
def show_category():
    categories=db.category_select()
    return ui.categoryShow(categories)

def category_validate(name=None):
    valid=""
    if name is not None:
        cat=db.category_select(name)
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
        categories=db.category_select()
        if validation:
            return ui.categoryShow(categories=categories, validation=validation, display="block")
        else:
            db.category_insert(name)
            categories=db.category_select()
            return ui.categoryAdd(categories)
    elif action=="delete":
        db.category_delete(request.forms.categoryname)
        categories=db.category_select()
        return ui.categoryAdd(categories)
    elif action=="edit":
        editId=db.category_select(request.forms.oldName)[0][0]
        validationEdit=category_validate(request.forms.nameEdit)
        if validationEdit:
            categories=db.category_select()
            return ui.categoryShow(categories=categories, validationEdit=validationEdit, editId=editId, displayEdit="block")
        else:
            db.category_update(request.forms.oldName, request.forms.nameEdit)
            categories=db.category_select()
            return ui.categoryAdd(categories)

    
        

