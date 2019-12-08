#PAra hacerlo solo con  los números de tu lista
def cuadrados():
	print ("Bienvenido a este programa, aquí se calculan los cuadrados de dos números enteros")
	n1= input('introduce un número entero n1 ')
	n1=int(n1)
	n2 = input('introduce un número entero n2 ')
	n2=int(n2)
	a = [n1,n2]
	b = []
	for i in a:
		{a = i * i,
		b.append(a)}
	print(b) 
	print('Adiós')

cuadrados()

#Para hacerlo con el rango de  todos los núeros dentro de los puestos como input
def cuadrados2():
	print ("Bienvenido a este programa, aquí se calculan los cuadrados de todos los números enteros dentro de un rango")
	n1= input('introduce el primer número de tu rango  ')
	n1=int(n1)
	n2 = input('introduce el último número de tu rangoº										 ')
	n2=int(n2)
	a = [n1,n2]
	b = []
	for i in range (n1,n2+1):
		a1 = i * i
		b.append(a1)
	print(b) 
	print('Adiós')

cuadrados2()
