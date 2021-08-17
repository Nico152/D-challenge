# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:51:36 2021

@author: nbafu
"""


import numpy as np


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


class Snake_Path:
    
    def __init__(self, board, snake):
        self.board = board
        self.snake = snake
        if (str(type(snake)) != "<class '__main__.Snake'>" and
            str(type(snake)) != "<class 'challenge.snake_game.Snake'>"):
            print("Attention: value not Snake class type")
        
    def get_move(self,direction):
        diccionario = {'U': [0,-1],
               'D': [0,1],
               'L': [-1,0],
               'R': [1,0]}
        try:
            return diccionario[direction]
        except:
            return ''
        
    def check_move(self, new_head):
        if (self.board[0] > new_head[0] and
            self.board[1] > new_head[1] and
            self.snake.can_move(new_head) and
            (new_head >= [0,0]).all()):
            return True
        else:
            return False
        
        
    def get_snake_paths(self, depth):
        if depth <= 0:
            return []
        else:
            paths_list = []
            directions = ['U','D','L','R']
            
            for d in directions:
                new_head = np.add(self.snake.get_head(), self.get_move(d))
                if self.check_move(new_head):
                    
                    new_snake = Snake(self.snake.get_new_body(new_head))
                    snake_path = Snake_Path(self.board, new_snake) 
                    results = snake_path.get_snake_paths(depth -1)
    
                    if results == [] :
                        paths_list.append(d)
                    else:
                        for i in results:
                            if len(i) == (depth-1):
                                path = d + ''.join([str(elem) for elem in i])
                                paths_list.append(path)
                
            return paths_list
        
    def get_number_different_snake_paths(self,depth):
        return len(self.get_snake_paths(depth))