import random
import sys
K = 10 
Q = 10
J = 10
A = 'A'
baraja = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J,]
B = random.choice(baraja)
C = random.choice(baraja)
house = random.choice(range(18,24))
print('Bienvenido a este juego. \n El objetivo es conseguir un número lo más cercano posible a 21, sin pasarse. \n Tus primeras cartas son: ', B, 'y', C)
if B == A:
	B = input('¿Qué valor quieres en A? ¿11 o 1? ')
if C == A:
	C = input('¿Qué valor quieres en A? ¿11 o 1? ')
B = int(B)
C = int(C)
suma = B + C
print('Tu suma es de ', suma)
if suma == 21:
	print('¡Ganaste!')
	sys.exit()
hitme = input("¿Quieres otra carta (S/N)? ")
while hitme == 'S':
	D = (random.choice(baraja))
	print(D)
	if D == A:
		D = input('¿Qué valor quieres en A? ¿11 o 1? ')
	D = int(D)
	suma = suma + D
	print('Tu suma es de ', suma)
	if suma > 21:
		print('Perdiste')
		sys.exit()
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