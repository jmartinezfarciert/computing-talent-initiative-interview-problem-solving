# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array will not contain duplicates.
#
# Note: If you know the number of times the array is rotated, then this problem
# becomes trivial. If the number of rotation is x, then minimum element is A[x].
#

def find_pivot_index(input_list):
# this is sorted, but then rotated
# find the minimum element in less than linear time
# return it's index
    min= input_list[1]
    for i in range(1,len(input_list)):
        # check the current index agains the previous index
        if input_list[i] < min:
            return i
print(
find_pivot_index([4, 5, 6, 7, 0, 1, 2])
)
