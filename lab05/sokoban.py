import os
from time import sleep
from adt import *

def sokoban_display(board):
    sleep(0)
    os.system('clear')
    print("#############")
    data = board_data(board)
    column = 0 
    edge = get_max(board,'x')
    for i in range(len(data)):
        print(data[i], end=' ')
        column += 1
        if column == edge:
            print()
            column = 0
            
    print("############")
def open_sokoban():   
    pass       
            
      
        

def play(): 
    board = create_board()          

    add_player(board, 0, 0)
    
    while True:   
        sokoban_display(board)
        dir = input(" ")
        player_direction(board, dir)
        print(board_data(board))
        if dir == "exit":
            break
  
    
    
play()