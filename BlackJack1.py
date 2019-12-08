#Se importan el paquete Random, que es el que se va a utilizar en el juego
#Es recomendarble correrlo desde la terminal de Linux, para mejores resultados
import random
#Primero se definen las variables J, K y Q que valen 10, así como la variable A, que puede tener dos valores
#Las variables son globales para que al salir de la función cambien las probabilidades con cada juego
K = 10 
Q = 10
J = 10
A = 'A'
#La lista viene con todas las cartas dentro de una baraja
baraja = [A, A, A, A, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, K, K, K, K, Q, Q, Q, Q, J, J, J, J]
def blackjack():
	
	#Las primeras dos cartas se eligen con random.choice
	#Después de sacar cada carta, esta se quita de la lista, con remove, de esta forma la misma carta no saldrá doble.
	PrimerCarta = random.choice(baraja)
	baraja.remove(PrimerCarta)
	SegundaCarta = random.choice(baraja)
	baraja.remove(SegundaCarta)
	#La mano de la casa se elige como un número al azar entre 18 y 24
	house = random.choice(range(18,24))
	print('Bienvenido a Black Jack. \n El objetivo es conseguir un número lo más cercano posible a 21, sin pasarse. \n Tus primeras cartas son: ', PrimerCarta, 'y', SegundaCarta)
	#Cuando se obtiene una carta A, se debe elegir el valor que se le va a dar
	if PrimerCarta == A:
		PrimerCarta = input('¿Qué valor quieres en A? ¿11 o 1? ')
	if SegundaCarta == A:
		SegundaCarta = input('¿Qué valor quieres en A? ¿11 o 1? ')
	PrimerCarta = int(PrimerCarta)
	SegundaCarta = int(SegundaCarta)
	suma = PrimerCarta + SegundaCarta
	print('Tu suma es de ', suma)
	#Si la suma es de 21, en automático se gana
	if suma == 21:
		print('¡Ganaste!')
		return None
	hitme = input("¿Quieres otra carta (S/N)? ")
	#Recuerda poner siempre la S mayúscula para que la función lo lea
	while hitme == 'S':
		Siguiente = (random.choice(baraja))
		print(Siguiente)
		baraja.remove(Siguiente)
		if Siguiente == A:
			Siguiente = input('¿Qué valor quieres en A? ¿11 o 1? ')
		Siguiente = int(Siguiente)
		suma = suma + Siguiente
		print('Tu suma es de ', suma)
		#Si la suma es mayor a 21, en automático se pierde. La única opción de ganar aquí es que la cas tenga un valor mayor a 21 también.
		if suma > 21:
			print('Perdiste')
			return None
		if suma == 21:
			print('¡Ganaste!')
			return None
		hitme = input('¿Quieres otra carta (S/N)?')
	if house == 21:
		print('Perdiste, gana la casa con 21, tu puntuación es de ', suma)
	elif house > suma and house < 22:
		print('Perdiste')
		print('Ganó la casa con ', house, ', tu puntuación fue de: ', suma)
	else:
		print ('¡Ganaste!')
		print ('La casa tiene', house, 'y tú tienes ', suma)
	print(baraja)	
blackjack()	

#Para repetir el juego, se usa la siguiente función, siempre se debe responder con S mayúscula para que lo lea. 

juego = input('¿Quieres volver a jugar? (S/N) ')
while juego == 'S':
	blackjack()
	juego = input('¿Quieres volver a jugar? (S/N) ')


