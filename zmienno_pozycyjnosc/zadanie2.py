def zad2():
	y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	z = list(reversed(y))
	x = [1, 1, 1, 1, 1, 1, 1, 1]
	for m in range(30): 
		for i in range(8):
			z[i] = (x[i] - y[i] - z[i])*10
	
	return z
print(zad2())
