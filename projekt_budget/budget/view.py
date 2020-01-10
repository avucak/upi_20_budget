from bottle import template

class CategoryView():

    @staticmethod
    def categoryShow(categories=[], validation="", validationEdit="", editId="", display="none", displayEdit ="none"):
        return template('categories', data=categories, validation=validation, validationEdit=validationEdit, editId=editId, disp=display, dispEdit=displayEdit)

    @staticmethod
    def categoryAdd(categories=[], validation="", validationEdit="", editId="", display="none", displayEdit="none"):
        return template('categories', data=categories, validation=validation, validationEdit=validationEdit, editId=editId, disp=display, dispEdit=displayEdit)
