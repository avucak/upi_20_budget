from bottle import Bottle, run, template, route
import control
# import os, sys

# dirname = os.path.dirname(sys.argv[0])


@route('/')
def index():
    return template('start')

run(host='localhost', port = 8080, debug=True, reloader=True)
