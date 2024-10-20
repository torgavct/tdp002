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
      
def sokoban_load(file,board):
    data = []
    file_data = open(file)
    data = file_data.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                add_wall(board, x, y)
            elif data[y][x] == 'o':
                add_box(board,x,y)
            elif data[y][x] == '.':
                add_storage(board,x,y)
            elif data[y][x] == '@':
                add_player(board, x, y)
    file_data.close()
    return board

def menu(): 
    os.system('clear')
    file1 = 'first_level.sokoban'
    file2 = 'second_level.sokoban'
    file3 = 'my_level.sokoban'
    while True:
        board = create_board()    
        try:
            print("Welcome to Sokoban, please choose a level:")  
            print("1. First level")
            print("2. Second level")
            print("3. My level")
            user_in = int(input("Chosse: "))
            if user_in == 1:
                sokoban_load(file1,board)
                print(board)
                play(board, file1)
                os.system('clear')
            elif user_in == 2:
                sokoban_load(file2 ,board)
                play(board,file2 )
                os.system('clear')
            elif user_in == 3:
                sokoban_load(file3,board)   
                play(board, file3)
                os.system('clear')
            else:
                os.system('clear')
                print("!!invalid input!!\n")
        except Exception as e:
            os.system('clear')
            print("!!invalid input!!\n")
        
def play(board, file):
    while True:
        sokoban_display(board) 
        if not check_win(board, file):
            print("Congratulations, You completed level'",file, "'!")
            input()
            break
        user_in = input("Make your move (a)left, (d)right, (w)up, (s)down: ") 
        if user_in == 'exit':
            break
        print()
        user_input(board, user_in)
    
    
    
    
    
menu()