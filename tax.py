def get_tax_by_(income):
	tax = 0
	if type(income)!= int:
		raise ValueError('Allow only numeric input')

	if 0 > income:
		return 0
	elif 0 < income < 1000:
		return 0
	elif 1000 < income < 10000:
		return 0 + .10*(income - 1000)
	elif 10000 < income < 20200:
		return 0 + .10*(10000 - 1000) + 0.15*(income - 10000)
	elif 20200 < income < 30750:
		return 0 + .10*(10000 - 1000) + 0.15*(20200 - 10000) + 0.20*(income - 20200)
	elif 30750 < income < 50000:
		return 0 + .10*(10000 - 1000) + 0.15*(20200 - 10000) + 0.20*(30750 - 20200) + 0.25*(50000 - 30750) + 0.30*(income - 50000)

		return tax

def calculate_tax(people):
	if type(people) is not dict:
		raise ValueError('The provided input is not a dictionary.')

	for person_name,income in people.iteritems():
		tax = get_tax_by_income(income)
		people[person_name] = tax

	return people
