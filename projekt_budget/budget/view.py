from bottle import template

class CategoryView():

    @staticmethod
    def categoryShow(categories=[]):
        return template('categories', data=categories)

    @staticmethod
    def categoryAdd(categories=[]):
        return template('categories', data=categories)
