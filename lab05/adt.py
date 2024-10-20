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
    board.append(['o',x,y])

def add_storage(board,x,y):
    board.append(['.',x,y])

def add_space(board,x,y):
    board.append([' ',x,y])
    
def add_player_on_storage(board,x,y):
    board.append(['+',x,y])
    
def add_box_on_storage(board, x,y):
    board.append(['*',x,y])

def board_data(board):
    for y in range(get_max(board, 'y')):
        for x in range(get_max(board, 'x')):
            add = True
            new_object = [' ', x, y]
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
    next_position = get_object(board, future_x, future_y)
    
    if next_position[0] == ' ':
        replace_object(board, current_position[1], current_position[2])
        remove_object(board,future_x , future_y)
        add_player(board, future_x, future_y)
        return board
    
    elif next_position[0] == 'o':
        next_box_pos = get_object(board, next_position[1]+x, next_position[2]+y)
        if next_box_pos[0] == ' ':
            replace_object(board, next_position[1], next_position[2])
            remove_object(board,next_box_pos[1], next_box_pos[2])
            add_box(board, next_box_pos[1], next_box_pos[2])
            
            replace_object(board, current_position[1], current_position[2])
            remove_object(board,future_x , future_y)
            add_player(board, future_x, future_y)
        elif next_box_pos[0] == '.':
            replace_object(board, next_position[1], next_position[2])
            remove_object(board,next_box_pos[1], next_box_pos[2])
            add_box_on_storage(board, next_box_pos[1], next_box_pos[2])
            
            replace_object(board, current_position[1], current_position[2])
            remove_object(board,future_x , future_y)
            add_player(board, future_x, future_y)
    
    elif  next_position[0] == '*':     
            
      
        return board 
        
        return board
    
    elif next_position[0] == '.':
        replace_object(board, current_position[1], current_position[2])
        remove_object(board,future_x , future_y)
        add_player_on_storage(board, future_x, future_y)
        return board 

def get_player_pos(board):
    for object in board:
        if object[0] == '@' or object[0] == '+':
            return object
    print("NO PLAYER FOUND")

def replace_object(board, x, y):
    for index in range(len(board)+1):
        object = board[index]
        if object[1] == x and object[2] == y:
            if object[0] == '+':
                object[0] = '.'
            elif object[0] == '*':
                object[0] = '.'
            else:
                object[0] = ' '
            return board
    return board

def remove_object(board, x, y):
    for object in board:
        if object[1] == x and object[2] == y:
            index = board.index(object)
            board.pop(index)
            return board
    return board

def move_box(board):
    pass