import numpy
from scipy.spatial import distance

mediaA = (3,3)
mediaB = (10,3)
mediaC = (10,10)

distanciaA = 0
distanciaB = 0
distanciaC =0
#El primer cochorte es de x de 0 a 6 con media de 3 y y igual.

def cohorteA():
	xa = numpy.random.randint(low=0, high=6, size=(10))
	ya = numpy.random.randint(low=0, high=6, size=(10))
	puntosA = [xa,ya]
	
	for list in puntosA:
		distancia = distance.euclidean(puntosA,mediaA)
		distanciaA = distanciaA + distancia 
	k = distanciaA/10
	print(k)
	
"""
def cohorteB():
	puntosB = numpy.random.randint(low=7, high=13, size=(10,2))
	
	
	
	
	for list in puntosB:
		distancia = distance.euclidean(puntosB,mediaB)
		distanciaB = distanciaB + distancia
	kb = distanciaB/10
	print(kb)

def cohorteC():
	puntosC = numpy.random.randint(low=7, high=13, size=(10,2))
	
	
	
	
	for list in puntosC:
		distancia = distance.euclidean(puntosC,mediaC)
		distanciaC = distanciaC + distancia
	kc = distanciaC/10
	print(kc)


un algoritmo que cuando metas un dato te indique a qué cohorte pertenece por su distancia con
todos los demás números; y por ver qué más cercano. 
	"""

cohorteA()
#cohorteB()
#cohorteC()

