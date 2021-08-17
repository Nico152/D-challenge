# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:01:17 2021

@author: nbafu
"""

import unittest

from challenge import snake_game as sg


class Test_Challenge(unittest.TestCase):
    def test_1(self):
        board = [4, 3]
        snake = sg.Snake([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])
        depth = 3

        snake_path  = sg.Snake_Path(board, snake)
        result = snake_path.get_number_different_snake_paths(depth)
        
        self.assertEqual(result, 7)
        
    def test_2(self):
        
        board = [2, 3]
        snake = sg.Snake([[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]])
        depth = 10
        
        snake_path  = sg.Snake_Path(board, snake)
        result = snake_path.get_number_different_snake_paths(depth)
        
        self.assertEqual(result, 1)
        
    def test_3(self):
        
        board = [10, 10]
        snake = sg.Snake([[5,5], [5,4], [4,4], [4,5]])
        depth = 4
        
        snake_path  = sg.Snake_Path(board, snake)
        result = snake_path.get_number_different_snake_paths(depth)
        
        self.assertEqual(result, 81)

if __name__ == '__main__':
    unittest.main()