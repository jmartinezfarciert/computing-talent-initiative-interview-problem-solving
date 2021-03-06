# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
# without repetition.

def validate_sudoku_board(board):
    #validate rows
    pass

def validate_row(row):
    # determine if there are any repeated numbers withi this list
    # create a container to hold the numbers 1-9
    seen_numbers = [False for x in row]
    # loop over every element in the row
    for element in row :
        # if you haven't seen this number before
        if element != "." :
            index = int(element)-1
            if not seen_numbers[index]:
                #add the number to the container
                seen_numbers[index] = True
            else:
                return False
    return True

print(
validate_row(["8","3",".",".","7",".",".",".","."]),
validate_row(["8","3",".",".","7",".",".","3","."])
)

# print(
# validate_sudoku_board(
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ])
# )

## Alternate half-assed solution
def validate_sudoku_board(board):
    #validate rows
    for row in board:
        temp = []
        temp[:] = row[:]
        temp.sort()
        temp.reverse()
        filled_boxes = []
        index_of_first_empty_box = temp.index(".")
        filled_boxes[:] = temp[:index_of_first_empty_box]
        if len(filled_boxes) != len(set(temp))-1:
            return False
    #validate columnds
    for coulumn_number in range(0, len(board)-1):
        column = []
        for row in board:
            column.append(row[coulumn_number])
        column.sort()
        column.reverse()
        filled_boxes = []
        index_of_first_empty_box = column.index(".")
        filled_boxes[:] = column[:index_of_first_empty_box]
        print(filled_boxes)
        if len(filled_boxes) != len(set(column))-1:
            return False
    return True
