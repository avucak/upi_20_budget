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

@post('/categories')
def add_category():
    name=request.forms.get('cname')
    db.category_insert(name)
    categories=db.category_select()
    return ui.categoryAdd(categories)

