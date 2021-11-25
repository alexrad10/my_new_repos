def find_max (mass):
	temp = mass[0]
	for element in mass:
		if element > temp:
			temp = element
	return temp