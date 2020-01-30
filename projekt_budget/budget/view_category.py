from bottle import template

class CategoryView():

    @staticmethod
    def categoryShow(categories=[], validation="", validationEdit="", editId="", display="none", deleteWarning=""):
        return template('categories', data=categories, validation=validation, validationEdit=validationEdit, editId=editId, disp=display, deleteWarning=deleteWarning)

