# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer
# of the previous row.
# Example:
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
#
# Given target = 3, return 1 ( 1 corresponds to true )
#
# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present )
 # for this problem
def matrix_search(matrix, target):
    sorted_list  = []
    for arr in matrix:
        sorted_list.extend(arr)

    start = 0
    end = len(sorted_list)
    while start < end :
        pivot = start + (end - start) // 2
        if sorted_list[pivot] > target:
            end = pivot
        if sorted_list[pivot] < target:
            start = pivot + 1
        if sorted_list[pivot] == target:
            return 1
    return 0

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target =
print(
matrix_search(matrix, target)
)

# Liz Howard's Solution
def matrix_search(matrix, target):

  rowIndex = 0

  while rowIndex < len(matrix):
    if matrix[rowIndex][0] <= target and matrix[rowIndex][-1] >= target:
      # it's in this row
      start = 0
      end = len(matrix[rowIndex])-1


      while start < end:
        pivot = ((end - start) // 2) + start
        if matrix[rowIndex][pivot] == target or matrix[rowIndex][end] == target:
          return 1
        if matrix[rowIndex][pivot] > target:
            end = pivot
        else:
            start = pivot + 1

      rowIndex += 1 # didn't find it in this row

    else:
      rowIndex += 1
  return 0
