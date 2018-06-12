""" birthdate is a library to assist in getting birthday values """

def get_value(min_value, max_value, prompt):
	while True:
		try:
			value = int(input(f'enter the {prompt} you were born: [{min_value} - {max_value}]: '))
			assert min_value <= value <= max_value
		except ValueError:
			print(f'not valid. try again.')
		except AssertionError: #add error prompt
			print(f"not a valid {prompt}. try again: ")
		else:
			return value

def birth_year():
	year = get_value(1000, 2018, 'year')
	return year

def birth_month():
	month = get_value(1, 12, 'month')
	return month

def birth_date():
	date = get_value(1, 30, 'date')
	return date

def birth_hour():
	hour = get_value(0, 24, 'hour')
	return hour

def birth_minute():
	minute = get_value(0, 60, 'minute')
	return minute

def birth_seconds():
	seconds = get_value(0, 60, 'seconds')
	return seconds

def get_birthdate():
	birthyear = birth_year()
	birthmonth = birth_month()
	birthday = birth_date()
	birthhour = birth_hour()
	birthminute = birth_minute()
	birthseconds = birth_seconds()
	birthdate = birthyear, birthmonth, birthday, birthhour, birthminute, birthseconds
	return birthdate