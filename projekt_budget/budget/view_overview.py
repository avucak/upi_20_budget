from bottle import template

class OverviewView():

    @staticmethod
    def overviewOptions(categories=[], minD="", maxD=""):
        return template('overview_options', categories=categories, minDate=minD, maxDate=maxD)

    @staticmethod
    def overviewReport(categories=[], minD="", maxD="", checkedCategories=[], fileName=""):
        return template('overview_report', categories=categories, minDate=minD, maxDate=maxD, checkedCategories=checkedCategories, fileName=fileName)

    @staticmethod
    def overviewShow(categories=[], transactions=[], checkedCategories=[], totalSum=[], totalAverage=[], pieChartData=[]):
        return template('overview', categories=categories, transactions=transactions, checkedCategories=checkedCategories, totalSum=totalSum, totalAverage=totalAverage, pieChartData=pieChartData)
