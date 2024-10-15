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

def get_coords(board,x,y):
    data = board_data(board)
    y = y*get_max(board,'y')
    for index in range(y,(y+get_max(board,'y')  )):
        if x == index:
            symbol = data[index]
            return symbol


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
        for i in range(get_max(board,'x')): 
            small_list.append(' ')
        for object in board:
            if object[2] == row:
                small_list[object[1]] = object[0]
        row+=1
        data = data + small_list
        small_list.clear()
    return data