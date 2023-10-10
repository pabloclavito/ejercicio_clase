#este es nuestro proyecto de python
class Persona:
	def __init__(self, nombre):
		self.nombre = nombre

class Bombero(Persona):
	def __init__(self, nombre, gustos):
		super().__init__(nombre)
		self.gustos = gustos

	def dialogo(self):
		print("Soy un bombero")
