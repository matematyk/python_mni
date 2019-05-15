class Vector():
	def __init__(self, *args):
		if len(args):
			self.values = args
		else:
			self.values = 0

	def __add__(self, other):
		x = (self.values + other)  
		return Vector(*x)
	def __repr__(self):
		return str(self.values) 



v = Vector(1,2,3)  # inicjalizacja - dowolna liczba argumentÃ³w
#v[2]   # 3
print(v) # wektor umie "się™" wypisywac
v + v   #  Vector(2,4,6)  lub ValueError("Wektory roznej dlugosci")
0 + v   #  Vector(0,1,2,3) 
v + 4   #  Vector(1,2,3,4)
