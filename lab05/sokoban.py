from adt import *

def sokoban_display():
    data = board_data(board)
    column = 0 
    edge = get_max(board,'x')
    for i in range(len(data)):
        print(data[i], end=' ')
        column += 1
        if column == edge:
            print()
            column = 0

 def open_sokoban():           
            
      
        

        
    
           
board = create_board()          
add_wall(board, x = 1, y = 0)
add_wall(board, x = 0, y = 1)
add_wall(board, x = 2, y = 1)
add_wall(board, x = 1, y = 2)
add_player(board, 1, 1)
sokoban_display()
coords = get_coords(board, 1, 1)
print(coords)
