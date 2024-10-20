#adt.py
import os

def create_board():
    return []
    
def add_wall(board, x, y):
    board.append(['#',x,y])
    return board

def add_player(board, x, y):
    board.append(['@',x,y])
    return board

def add_box(board,x,y):
    board.append(['0',x,y])

def add_storage(board,x,y):
    board.append(['.',x,y])

def add_space(board,x,y):
    board.append(['?',x,y])

def board_data(board):
    for y in range(get_max(board, 'y')):
        for x in range(get_max(board, 'x')):
            add = True
            new_object = ['?', x, y]
            for object in board:
                if new_object[1]==object[1] and new_object[2] == object[2]:
                    add = False
            if add:       
                board.append(new_object)  
    return board

def get_max(board, n):
    if n == 'x': n = 1
    if n == 'y': n = 2
    n_values = []
    max_n = 0
    for index in board:
        n_values.append(index[n])
    n_values.sort() 
    max_n += n_values[len(n_values)-1]+1
    return max_n

def get_object(board,x,y):
    for object in board:
        if object[1] == x and object[2] == y:
            return object
    
    return board

def player_input(board, input):
    if input.lower() == 'w':
        move_player(0,-1, board) 
    elif input.lower() == 'a':
        move_player(-1,0,board)   
    elif input.lower() == 's':
        move_player(0,1,board)
    elif input.lower() == 'd':
        move_player(1,0,board)    

def move_player(x, y, board):
    current_position = get_player_pos(board)
    future_x = current_position[1]+x
    future_y = current_position[2]+y
    print("here")
    next_position = get_object(board, future_x, future_y)
    print(next_position)
    
    if next_position[0] == '?':
        print("here")
        
    
        remove_item(board, current_position[1], current_position[2])
        add_player(board, future_x, future_y)
    return board

def get_player_pos(board):
    for object in board:
        if object[0] == '@':
            return object
    print("NO PLAYER FOUND")

def remove_item(board, x, y):
    for index in range(len(board)+1):
        object = board[index]
        if object[1] == x and object[2] == y:
            board.index(object)
            board.pop()
            return board
    return board