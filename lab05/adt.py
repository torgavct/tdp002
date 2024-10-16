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
    board.append([' ',x,y])

def get_position(board,x,y):
    data = board_data(board)
    iteration = 0
    for i in range(0,len(data),get_max(board,'x')):
        chunk = data[i:i+get_max(board,'y')]
        if iteration == y:
            return chunk[x]
        iteration+=1

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

def board_data(board):
    data = []
    row = 0
    small_list = []
    while row < get_max(board, 'y'):
        for i in range(get_max(board,'y')): 
            small_list.append(' ')
        for object in board:
            if object[2] == row:
                small_list[object[1]] = object[0]
        row+=1
        data = data + small_list
        small_list.clear()
    return data

def move_box(board, x, y):
    print("move box")
    pass

def player_direction(board, dir):
    if dir.lower() == 'w':
        move(0,-1, board)
           
    elif dir.lower() == 'a':
        move(-1,0,board)
            
    elif dir.lower() == 's':
        move(0,1,board)
            
    elif dir.lower() == 'd':
        move(1,0,board)
           
    
def move(dir_x, dir_y, board):
    player = player_pos(board)
    new_x = player[1]+dir_x
    new_y = player[2]+dir_y
    try:
        new_pos = get_position(board,new_x,new_y)
    except:
        return board
    if new_pos == ' ':
        remove_item(board, player[1], player[2])
        add_player(board,new_x,new_y)
        return board
    elif new_pos == '0':
        move_box(board,)
    return board

def player_pos(board):
    for object in board:
        if object[0] == '@':
            return object
    print("NO PLAYER FOUND")

def remove_item(board, x, y):
    for index in board:
        if index[1] == x and index[2] == y:
            item = board.index(index)
            board.pop(item)
            return board
    