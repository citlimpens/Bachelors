class Perros:
	def imprimenombre(self):
		print('Esta clase incluye perros')
	def __init__(self):
		self.conteo = 0
		self.chihuahuas = 0
		self.grandanes = 0

class Chihuahuas(Perros):
	def conteochihuahuas(self):
		self.chihuahuas += 1
		print('Ahora hay ', self.chihuahuas, 'chiahuahuas')
		self.conteo == self.chihuahuas
		print('Ahora hay ', self.conteo, 'perros en total')

class GranDanes(Perros):
	def conteograndanes(self):
		self.grandanes += 1
		print('Ahora hay ', self.grandanes, 'Gran daneses')
		self.conteo = self.chihuahuas + self.grandanes
		print('Ahora hay ', self.conteo, 'perros en total')

C = Chihuahuas()
GD = GranDanes()

C.conteochihuahuas()
C.conteochihuahuas()
C.conteochihuahuas()
C.conteochihuahuas()


GD.conteograndanes()

