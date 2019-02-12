from .controller import Report

def getReport(*args, **kwargs):

    return Report().get_reports(kwargs['searchString'])

def getReportByID(*args, **kwargs):
    print('args: %r' % str(args))
    print('kwargs: %r' % kwargs)
    print('getReportById')