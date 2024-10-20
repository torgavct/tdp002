import os
from time import sleep
from adt import *

def sokoban_display(board):
    os.system('clear')
    data = board_data(board)
    for y in range(get_max(board, 'y')):
        for x in range(get_max(board, 'x')):
            for object in board:
                if object[1] == x and object[2] == y:
                    print(object[0], end=' ')
                else:
                    continue
        print()
      
def sokoban_load(file,board):
    file_data = open(file)
    file_data = file_data.readlines()
    for y in range(len(file_data)):
        for x in range(len(file_data[y])):
            if file_data[y][x] == ' ':
                add_space(board, x,y)
            elif file_data[y][x] == '#':
                add_wall(board, x, y)
            elif file_data[y][x] == 'o':
                add_box(board,x,y)
            elif file_data[y][x] == '.':
                add_storage(board,x,y)
            elif file_data[y][x] == '@':
                add_player(board, x, y)
    return board

def play(): 
    board = create_board()    
    sokoban_load('first_level.sokoban',board)
    while True:   
        sokoban_display(board)
        user_input = input(" ")
        player_input(board, user_input)
        print(board)
        if dir == "exit":
            break
  
    
    
play()