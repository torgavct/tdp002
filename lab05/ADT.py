wall = "#"
spelare = "@"
box = "0"
storage = "."
floor = " "

def create_board():
    return []
    
def add_wall(board, x, y):
    print("here")
    while len(board) <= y:
        board.append([])
        print("here")
    while len(board[y]) <= x:
        board.append("")
        print("yhere")
    print("ute")
    board[y][x]

def add_player(board, x, y):
    #add_object(board, spelare, x, y)
    pass

def add_box(board, x, y):
    #add_object(board, box, x, y)
    pass

def add_storage(board , x, y):
    #add_object(board, storage, x ,y)
    pass
def create_player():
    #return player
    pass
  

board = create_board()
add_wall(board, x = 1, y = 0)
add_wall(board, x = 0, y = 1)
add_wall(board, x = 2, y = 1)
add_wall(board, x = 1, y = 2)
print(board)