import numpy as np 
import random as rd

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
					 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Palabras = dict()
coordenadas_importantes = dict()

direccion = [
		(-1, 0),  # 'up'
		(+1, 0),  # 'down'
		(0, +1),  # 'right'
		(0, -1),  # 'left'
		(-1, +1),  # '↗'
		(+1, +1),  # '↘'
		(-1, -1),  # '↖'
		(+1, -1)  # '↙'
]


class SopaPalabras():
	def __init__(self, size_x, size_y):
		self.size_x = size_x
		self.size_y = size_y
		
		self.matriz = np.zeros((self.size_x, self.size_y), dtype=str).tolist()
		self.matrizFinal = np.zeros((self.size_x, self.size_y), dtype=str).tolist()
		
		self.lista_x = []
		self.lista_y = []
		
		self.lista_palabras = []
		self.llenar_sopa_letras()
		self.llenar_sopa_simbolos()
		
	def llenar_sopa_letras(self):
		for row in range(len(self.matriz)):
			for elemets in range(len(self.matriz[row])):
				self.matrizFinal[row][elemets] = random.choice(letters)
	
	def llenar_sopa_simbolos(self):
		for row in range(len(self.matriz)):
			for elemets in range(len(self.matriz[row])):
				self.matrizFinal[row][elemets] = random.choice('-') 
	
	def checar_xy(self, x, y):
		if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]):
			return True
		else: 
			return False
		
	def inicio_xy(self):
		self.inicio_x = rd.randint(0, self.size_x - 1)
		self.inicio_y = rd.randint(0, self.size_y - 1)

	def fin_xy(self):
		longitud = len(self.palabra)-1
		self.x_fin = 0
		self.y_fin = 0
		while True:
			self.random_direcction = random.sample(direccion, len(direccion))
			self.random_direcction.append('*')
			for i in self.random_direcction:
				if i == '*':
					self.inicio_xy()
					break
				self.direccion_x = i[0]
				self.direccion_y = i[1]
				self.x_fin = self.x_inicio + (self.direccion_x * longitud)
				self.y_fin = self.y_inicio + (self.direccion_y * longitud)
				
				if (self.checar_coordenadas(self.x_fin, self.y_fin) == True):
					return self.direccion_x, self.direccion_y, self.x_fin, self.y_fin
			if i == '*':
				continue
	
	
	