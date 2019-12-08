#Se importan los paquetes Random y Sys, que son los que se van a utilizar en el juego
#Es recomendarble correrlo desde la terminal de Linux, para mejores resultados
import random
import sys
def blackjack():
	#Primero se definen las variables J, K y Q que valen 10, así como la variable A, que puede tener dos valores
	K = 10 
	Q = 10
	J = 10
	A = 'A'
	#La lista viene con todas las cartas dentro de una baraja
	baraja = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J]
	#Las primeras dos cartas se eligen con random.choice
	B = random.choice(baraja)
	C = random.choice(baraja)
	#La mano de la casa se elige como un número al azar entre 18 y 24
	house = random.choice(range(18,24))
	print('Bienvenido a Black Jack. \n El objetivo es conseguir un número lo más cercano posible a 21, sin pasarse. \n Tus primeras cartas son: ', B, 'y', C)
	#Cuando se obtiene una carta A, se debe elegir el valor que se le va a dar
	if B == A:
		B = input('¿Qué valor quieres en A? ¿11 o 1? ')
	if C == A:
		C = input('¿Qué valor quieres en A? ¿11 o 1? ')
	B = int(B)
	C = int(C)
	suma = B + C
	print('Tu suma es de ', suma)
	#Si la suma es de 21, en automático se gana
	if suma == 21:
		print('¡Ganaste!')
		sys.exit()
	hitme = input("¿Quieres otra carta (S/N)? ")
	#Recuerda poner siempre la S mayúscula para que la función lo lea
	while hitme == 'S':
		D = (random.choice(baraja))
		print(D)
		if D == A:
			D = input('¿Qué valor quieres en A? ¿11 o 1? ')
		D = int(D)
		suma = suma + D
		print('Tu suma es de ', suma)
		#Si la suma es mayor a 21, en automático se pierde. La única opción de ganar aquí es que la cas tenga un valor mayor a 21 también.
		if suma > 21:
			print('Perdiste')
			break 
		if suma == 21:
			print('¡Ganaste!')
			sys.exit()
		hitme = input('¿Quieres otra carta (S/N)?')
	if house > suma and house < 22:
		print('Perdiste')
		print('Ganó la casa con ', house, ', tu puntuación fue de: ', suma)
	else:
		print ('¡Ganaste!')
		print ('La casa tiene', house, 'y tú tienes ', suma)	
blackjack()	

#Para repetir el juego, se usa la siguiente función, siempre se debe responder con S mayúscula para que lo lea. 

juego = input('¿Quieres volver a jugar? (S/N) ')
while juego == 'S':
	blackjack()
	juego = input('¿Quieres volver a jugar? (S/N) ')

