from bottle import template

class CategoryView():

    @staticmethod
    def categoryShow(categories=[], validation="", display="none"):
        return template('categories', data=categories, validation=validation, disp=display)

    @staticmethod
    def categoryAdd(categories=[], validation="", display="none"):
        return template('categories', data=categories, validation=validation, disp=display)
