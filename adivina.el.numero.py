#Juego de adivina un número
import random
import math
def AdivinaElNumero():
	print('Bienvenido a Adivina el Numero')
	Rango = input('Tu rango irá de 1 a...')
	Rango = int(Rango)
	Numero = random.choice(range(1, Rango + 1))
	contador = math.floor(math.log2(Rango))
	while contador > 0:
		NumAdivinado = input('Adivina un número: ')
		NumAdivinado = int(NumAdivinado)
		if NumAdivinado == Numero:
			print('Ganaste, adivinaste el número')
			break
		elif NumAdivinado > Numero:
			print('Tu número es mayor al que estoy pensando \n Te quedan: ', contador - 1, 'oportunidades')
		else:
			print('Tu número es menor al que estoy pensando \n Te quedan: ', contador - 1, 'oportunidades')
		contador -= 1
	if contador == 0:
		print('Perdiste. \n El número era: ', Numero)

AdivinaElNumero()

juego = input('¿Quieres volver a jugar? (S/N) ')
while juego == 'S':
	AdivinaElNumero()
	juego = input('¿Quieres volver a jugar? (S/N) ')