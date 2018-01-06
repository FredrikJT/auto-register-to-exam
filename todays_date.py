import datetime

def todays_date():
    mylist = []
    today = datetime.date.today()
    mylist.append(today)
    return str(mylist[0])