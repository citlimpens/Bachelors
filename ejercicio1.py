def hipotenusa():
	print('Este programa calcula la distancia euclideana entre dos puntos')
	c1 = input('Cuánto mide tu cateto 1?')
	c2 = input('Cuánto mide tu cateto 2?')
	cuadrados = ((float(c1)) * (float(c1))) + ((float(c2))*(float(c2)))
	print(cuadrados)
	d = cuadrados ** .5
	print('Tu distancia es de: ', d)

hipotenusa()