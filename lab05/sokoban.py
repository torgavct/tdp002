import os
from time import sleep
from adt import *

def sokoban_display(board):
    data = board_data(board)
    for y in range(get_max(board, 'y')):
        for x in range(get_max(board, 'x')):
            for object in board:
                if object[1] == x and object[2] == y:
                    print(object[0], end=' ')
                else:
                    continue
        print()
      
        

def play(): 
    board = create_board()    
    add_player(board, 0, 0)      
    add_space(board, 2, 2)
    
    
    while True:   
        sokoban_display(board)
        user_input = input(" ")
        player_input(board, user_input)
        print(board)
        if dir == "exit":
            break
  
    
    
play()