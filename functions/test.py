

class Test:
	def __init__(self, mas):
		self.mas = mas
		self.test = [[]]

	def chenge(self):
		self.mas[0][1] = 488

	def getMas(self):
		return self.mas


mas = [[10, 20], [21, 43], "sdfsdf"]

#print(mas)

#mas.append(200)
#print(mas[2][0])

#print(mas)
test = Test(mas)
#print(len(test.test))

for m in mas[1:]:
	print(m)



#mas1 = test.getMas()
#mas1[0][0] = 488


#print(mas)
