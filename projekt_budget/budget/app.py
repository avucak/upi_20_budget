from bottle import Bottle, run, template, route
import control_category, control_transaction, control_overview

@route('/')
def index():
    return template('start')

run(host='localhost', port = 8080, debug=True, reloader=True)
