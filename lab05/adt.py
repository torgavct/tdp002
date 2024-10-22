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

def user_input(board, input):
    if input.lower() == 'w':
        available = player_can_move(0,-1, board)
        if available:
            move_player(0,-1,board)
    elif input.lower() == 'a':
        available = player_can_move(-1,0, board)
        if available:
            move_player(-1,0,board)
    elif input.lower() == 's':
        available = player_can_move(0,1, board)
        if available:
            move_player(0,1,board)
    elif input.lower() == 'd':
        available = player_can_move(1,0, board)
        if available:
            move_player(1,0,board)
    return board

def move_player(x, y, board):
    player_position = get_player_pos(board)
    next_x = player_position[1] + x
    next_y = player_position[2] + y
    next_position = get_object(board, next_x, next_y)
    if player_position[0] == '+':
        replace_object(board, player_position, '.')
    else:
        replace_object(board, player_position, ' ')     
    remove_object(board,  next_position[1], next_position[2])
    if next_position[0] == ' ':
        add_player(board, next_position[1], next_position[2])
    elif next_position[0] == '.':
        add_player_on_storage(board, next_position[1], next_position[2])
    return board


def move_box(board, box_position,move_x, move_y):
    next_x = box_position[1] + move_x
    next_y = box_position[2] + move_y
    next_position = get_object(board, next_x, next_y)
    remove_object(board,  next_position[1], next_position[2])
    if box_position[0] == '*':
        replace_object(board, box_position, '.')
    else:
        replace_object(board, box_position, ' ')  
    if next_position[0] == ' ':
        add_box(board, next_position[1], next_position[2])
    elif next_position[0] == '.':
        add_box_on_storage(board, next_position[1], next_position[2])
    return board


def get_player_pos(board):
    for object in board:
        if object[0] == '@' or object[0] == '+':
            return object
    print("NO PLAYER FOUND")
    return None

def replace_object(board, object, replace):
    for matching_object in board:
        if matching_object[1] == object[1] and matching_object[2] == object[2]:
            matching_object[0] = replace
    return board

def remove_object(board, x, y):
    for object in board:
        if object[1] == x and object[2] == y:
            index = board.index(object)
            board.pop(index)
            return board
    return board

def check_win(board, file):
    marked_spots = 0
    for object in board:
        if object[0] == '.':
            marked_spots += 1
    if marked_spots == 0:
        return False
    return True


def player_can_move(x, y, board):
    player_position = get_player_pos(board)
    next_x = player_position[1] + x
    next_y = player_position[2] + y
    next_position = get_object(board, next_x, next_y)
    if next_position[0] == ' ': return True
    elif next_position[0] == '#': return False
    elif next_position[0] == 'o':
        move = box_can_move(next_position,x, y, board)
        if move:
            move_box(board,next_position,x,y)
            return True
    elif next_position[0] == '*':
        move = box_can_move(next_position,x, y, board)
        if move:
            move_box(board,next_position,x,y)
            return True
    elif next_position[0] == '.': return True
    return False

def box_can_move(box_position,x, y, board):
    next_x = box_position[1] + x
    next_y = box_position[2] + y
    next_position = get_object(board, next_x, next_y)   
    if next_position[0] == ' ':return True
    elif next_position[0] == '.':return True
    elif next_position[0] == 'o':return False
    elif next_position[0] == '#':return False
    return False