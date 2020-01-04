from bottle import Bottle, run, template, route
import control
# import os, sys

# dirname = os.path.dirname(sys.argv[0])


@route('/')
def index():
    return template('start')

@route('/transactions')
def index1():
    return template('transactions')





run(host='localhost', port = 8080, debug=True)
