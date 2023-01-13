from datetime import datetime

def date(date1,date2):
	d1 = datetime.strptime(date1,'%Y/%m/%d')
	d2 = datetime.strptime(date2,'%Y/%m/%d')
	return d1-d2

def time(time1,time2):
	t1 = datetime.strptime(time1,'%H:%M:%S')
	t2 = datetime.strptime(time2,'%H:%M:%S')
	return t1-t2