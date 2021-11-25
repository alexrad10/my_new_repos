N = int(input())  # size of massive
new_mass = []
for i in range(N):
	new_mass.append(int(input()))
val = find_max(new_mass)

def find_max (mass):
	temp = mass[0]
	for element in mass:
		if element < temp:
			temp = element
	return temp