# Leap year occurs in every year divisible by 4
# EXCEPT every year evenly divisible by 100
# UNLESS evenly divisible by 400

def is_leap_year(year):
	div_by_100 = year % 100
	div_by_400 = year % 400
	div_by_4 = year % 4

	if div_by_4 == 0:
		if div_by_100 == 0:
			if div_by_400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False



