# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:51:36 2021

@author: nbafu
"""


import numpy as np

# Clase Snake, representa el cuerpo de la serpiente dentro del tablero. Permite
# verificar si puede hacer un movimiento sin cruzarse consigo misma y permite obtener
# el nuevo cuerpo despues de mover la cabeza. 

class Snake:
    
    def __init__(self, body):
        self.body = body

    def get_head(self):
        return self.body[0] 
    
    def can_move(self, new_head):
        for i in self.body[:-1]:
            if (i == new_head).all():
                return False
        return True
    
    def get_new_body(self,new_head):
        return [new_head] + self.body[:-1]


# Clase Snake Path, representa el tablero y la serpiente, permite calcular el número
# de caminos que puede hacer la serpiente en una longitud o profundidad determinada.

class Snake_Path:
    
    def __init__(self, board, snake):
        self.board = board
        self.snake = snake
        

    # Mediante la función get_move, obtenemos las coordenadas a sumar a la nueva cabeza
    # en función de la dirección indicada.
    def get_move(self,direction):
        diccionario = {'U': [0,-1],
               'D': [0,1],
               'L': [-1,0],
               'R': [1,0]}
        
        return diccionario[direction]
        
    
    # Mediante la función check_move, verificamos que el nuevo movimiento de la serpiente
    # se encuentra dentro de los límites del tablero y no choca con otras partes de su cuerpo.
    def check_move(self, new_head):
        if (self.board[0] > new_head[0] and
            self.board[1] > new_head[1] and
            self.snake.can_move(new_head) and
            (new_head >= [0,0]).all()):
            return True
        else:
            return False
        
    
    # Mediante la función get_snake_paths, obtenemos todos los posibles caminos que puede
    # tomar la serpiente en función de una determinada profundidad.
    
    def get_snake_paths(self, depth):
        
        # Si la profundidad del camino es 0, no se puede mover más.
        
        if depth <= 0:
            return []
        else:
            
            # Declaramos las variables de los posibles caminos a registrar
            # así como las direcciones a tomar.
            paths_list = []
            directions = ['U','D','L','R']
            
            # Para cada posible dirección a tomar, calculamos la posible nueva 
            # cabeza de la serpiente una vez realizado el movimiento.
            
            for d in directions:
                new_head = np.add(self.snake.get_head(), self.get_move(d))
                
                #Antes de hacer nada, verificamos si el movimiento es factible.
                
                if self.check_move(new_head):
                    
                    # Calculamos nuevo cuerpo de la serpiente una vez realizado
                    # el movimiento.
                    new_snake = Snake(self.snake.get_new_body(new_head))
                    
                    # Procedemos a calcular que siguientes direcciones puede tomar
                    # la serpiente con el nuevo cuerpo.
                    snake_path = Snake_Path(self.board, new_snake) 
                    results = snake_path.get_snake_paths(depth -1)
    
                    if results == [] :
                        #Si no se ha pueden tomar más direcciones válidas 
                        # después de la dirección tomada, se añade a la lista de caminos.
                        paths_list.append(d)
                    else:
                        # Para cada posible camino tomado después del movimiento,
                        # verificamos si es de la longitud/profundidad indicada
                        # depth - 1. Si es así se añade a la lista de caminos válidos junto
                        # con la dirección de movimiento elegida. 
                        for i in results:
                            if len(i) == (depth-1):
                                path = d + ''.join([str(elem) for elem in i])
                                paths_list.append(path)
                
            return paths_list
        
    # Mediante la siguiente función, obtenemos el número de total de posibles caminos
    # a tomar por la serpiente para una profundida determinada.
    def get_number_different_snake_paths(self,depth):
        return len(self.get_snake_paths(depth))