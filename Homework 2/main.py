
sudoku = [
    [5, 3,-1, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0,-1, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, -1, 0, 7, 9]
]

sudoku_2 = [
    [-1, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, -1, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, -1]
]

sudoku_3 = [
    [ 8, 4, 0, 0, 5, 0, 0, 0, 0],
    [ 3, 0, 0, 6, 0, 8, 0, 4, 0],
    [ 0, 0, 0, 4, 0, 9, 0, 0, 0],
    [ 0, 2, 3, 0, 0, 0, 9, 8, 0],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 4],
    [ 0, 9, 8, 0, 0, 0, 1, 6, 0],
    [ 0, 0, 0, 5, 0, 3, 0, 0, 0],
    [ 0, 3, 0, 1, 0 ,6, 0, 0, 7],
    [ 0, 0, 0, 0, 2, 0, 0, 1, 3]
]

sudoku_final_test = [
    [ 8, 4, 0, 0, 5, 0,-1, 0, 0],
    [ 3, 0, 0, 6, 0, 8, 0, 4, 0],
    [ 0, 0,-1, 4, 0, 9, 0, 0,-1],
    [ 0, 2, 3, 0,-1, 0, 9, 8, 0],
    [ 1, 0, 0,-1, 0,-1, 0, 0, 4],
    [ 0, 9, 8, 0,-1, 0, 1, 6, 0],
    [-1, 0, 0, 5, 0, 3,-1, 0, 0],
    [ 0, 3, 0, 1, 0 ,6, 0, 0, 7],
    [ 0, 0,-1, 0, 2, 0, 0, 1, 3]
]




evil   = [[0, 6, 0, 8, 0, 0, 0, 0, 0],
              [0, 0, 4, 0, 6, 0, 0, 0, 9],
              [1, 0, 0, 0, 4, 3, 0, 6, 0],
              [0, 5, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 8, 6, 0, 9, 3, 0, 0],
              [0, 0, 0, 0, 0, 0, 5, 7, 0],
              [0, 1, 0, 4, 8, 0, 0, 0, 5],
              [8, 0, 0, 0, 1, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 5, 0, 4, 0]]

easy   = [[0, 3, 0, 0, 8, 0, 0, 0, 6],
              [5, 0, 0, 2, 9, 4, 7, 1, 0],
              [0, 0, 0, 3, 0, 0, 5, 0, 0],
              [0, 0, 5, 0, 1, 0, 8, 0, 4],
              [4, 2, 0, 8, 0, 5, 0, 3, 9],
              [1, 0, 8, 0, 3, 0, 6, 0, 0],
              [0, 0, 3, 0, 0, 7, 0, 0, 0],
              [0, 4, 1, 6, 5, 3, 0, 0, 2],
              [2, 0, 0, 0, 4, 0, 0, 6, 0]]

medium = [[3, 0, 8, 2, 9, 6, 0, 0, 0],
              [0, 4, 0, 0, 0, 8, 0, 0, 0],
              [5, 0, 2, 1, 0, 0, 0, 8, 7],
              [0, 1, 3, 0, 0, 0, 0, 0, 0],
              [7, 8, 0, 0, 0, 0, 0, 3, 5],
              [0, 0, 0, 0, 0, 0, 4, 1, 0],
              [1, 2, 0, 0, 0, 7, 8, 0, 3],
              [0, 0, 0, 8, 0, 0, 0, 2, 0],
              [0, 0, 0, 5, 4, 2, 1, 0, 6]]

hard   = [[7, 0, 0, 0, 0, 0, 0, 0, 0],
              [6, 0, 0, 4, 1, 0, 2, 5, 0],
              [0, 1, 3, 0, 9, 5, 0, 0, 0],
              [8, 6, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 1, 0, 0, 0, 4, 0, 5],
              [0, 0, 0, 0, 0, 0, 0, 8, 6],
              [0, 0, 0, 8, 4, 0, 5, 3, 0],
              [0, 4, 2, 0, 3, 6, 0, 0, 7],
              [0, 0, 0, 0, 0, 0, 0, 0, 9]]






def get_valid_values(board, row, col):

    values = [False] * 10
    values[0] = True

    #print(values)
    
    for i in range(9):
        # Verifica linia
        val = board[row][i]
        if val != -1:
            values[val] = True

        # Verifica coloana
        val = board[i][col]
        if val != -1:
            values[val] = True
            
    # Verifica regiunea 3x3
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            val = board[i + startRow][j + startCol]
            values[val] = True

    #pune intr-o lista totii indexi ce au valoare = False (tratez si cazul cu -1 in care returnez doar indexii pari)
    val_row_col = board[row][col]
    result = [index for index , val in enumerate(values) if val == False and (val_row_col == 0 or index % 2 == 0) ]

    return result

def forward_checking(board , history_list = []):

    # a list of tuples : [ (row , column , [valid_values_to_choose_from] ) ]
    uncompleted_values_info = []

    for i in range(9):
        for j in range(9):
            if board[i][j] < 1:
                valid_values = get_valid_values(board,i,j)
                if valid_values == []:
                    return None
                #we have a cell where we cant choose anything
                uncompleted_values_info.append(( i , j , valid_values))

    #check if all cells are completed
    if uncompleted_values_info == []:
        return board
    
    #sort choices based on MRV (we sort based on the number of posibilites of each cell because we want to start completing the cell with the smallest set of possibilities)
    sorted_uncompleted_values_info = sorted(uncompleted_values_info ,  key = lambda element : len(element[2]))

    for value_info in sorted_uncompleted_values_info:
        row , col , valid_values = value_info

        for value in valid_values:

            #make a copy of the board
            board_copy = [list(sublist) for sublist in board]

            #complete the cell of the copy
            board_copy[row][col] = value

            #print(len(history_list))
            #print(history_list)
            #print_sudoku(board_copy)

            #forward_checking recursively
            result = forward_checking(board_copy , history_list = history_list + [(row,col,value)])

            #check if we have a good solution
            if result is not None:
                return result
        
        return None

    return None

def print_sudoku(board):
    print("This is a sudoku board :")
    return [print(sublist) for sublist in board]

solution = forward_checking(sudoku_final_test)
print_sudoku(solution)
