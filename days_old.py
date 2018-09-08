def leapyear(year):
	if year%400==0:
		return True
	if year%100==0:
		return False
	if year%4==0:
		return True
	else:
		return False


def monthdays(year,month):
	if month==9 or month==4 or month==6 or month==11:
		days=30
	if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
		days=31
	if month==2:
		if leapyear(year):
			days=29
		else:
			days=28
	return days


def nextDay(year,month,day):
	if day<=monthdays(year,month):
		day=day+1
	if day>monthdays(year,month):
		day=1
		month=month+1
		if month>12:
			month=1
			year=year+1
	return (year,month,day)


def isBefore(year1,month1,day1,year2,month2,day2):
	if year1<year2:
		return True
	if year1==year2:
		if month1<month2:
			return True
		if month1==month2:
			if day1<day2:
				return True
	else:
		return False


def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	agedays=0
	assert isBefore(year1,month1,day1,year2,month2,day2)
	while isBefore(year1,month1,day1,year2,month2,day2):
		year1,month1,day1=nextDay(year1,month1,day1)
		agedays=agedays+1
	return agedays