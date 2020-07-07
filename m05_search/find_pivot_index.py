# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array will not contain duplicates.
#
# Note: If you know the number of times the array is rotated, then this problem
# becomes trivial. If the number of rotation is x, then minimum element is A[x].
#
#Less than linear time using binary search
def find_pivot_index(input_list):
    start_index = 0
    end_index = len(input_list)-1
    minimum_index = 0

    while start_index < end_index - 1 :
        test_index = int((end_index - start_index) / 2) + start_index
        if input_list[test_index] < input_list[minimum_index]:
            minimum_index = test_index
            end = test_index
        else :
            start_index = test_index
    return minimum_index
    
print(
find_pivot_index([4, 5, 6, 7, 0, 1, 2])
)

# Linear time
def find_pivot_index(input_list):
    min= input_list[0]
    for i in range(1,len(input_list)):
        # check the current index agains the previous index
        if input_list[i] < min:
            return i
