


massive = [[10, 13, 20, 10],
		   [40, 10, 32]]

print(massive)

for mas in massive:
	for index in enumerate(mas):
		if index[1] == 10 and len(mas) != index[0] + 1:
			mas[index[0] + 1] = 11

print(massive)
