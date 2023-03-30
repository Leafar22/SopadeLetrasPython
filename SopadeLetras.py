import numpy as np 
import random as rd

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
					 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direccion = [
		(-1, 0),  # 'up'
		(+1, 0),  # 'down'
		(0, +1),  # 'right'
		(0, -1),  # 'left'
		(-1, +1),  # '↗'
		(+1, +1),  # '↘'
		(-1, -1),  # '↖'
		(+1, -1)  #  '↙'
]
