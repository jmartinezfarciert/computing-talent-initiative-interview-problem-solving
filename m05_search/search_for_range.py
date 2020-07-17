# Given a sorted A of integers, find the starting and ending position of
# a given B value.
# Your algorithm’s runtime complexity must Be in the order of O(log n).
# If the B is not found in the A, return [-1, -1].
# Example:
# Given [5, 7, 7, 8, 8, 10]
# and B value 8,
# return [3, 4].
# #Liz Howard's solution
# def find_index(sorted_list, B):
#     start, end = 0, len(sorted_list)
#     while start < end:
#         pivot = start + (end - start) // 2
#         if sorted_list[pivot] < B:
#             start = pivot + 1
#         else:
#             end = pivot
#             return start

def search_for_range(A, B):
    start = 0
    end = len(A)
    # search for starting range_index
    minIndex = 0
    while start < end -1 :
        if (end - start) % 2 == 0:
            pivot = (end - start) // 2 + start
        else :
            pivot = (end - start + 1) // 2 + start

        if A[pivot] == B :
            minIndex = pivot
            end = minIndex
        if A[pivot] < B :
            start = pivot
        else :
            end = pivot
    if A[0] == B:
        minIndex = 0
    # search for ending range_index
    maxIndex = 0
    end = len(A)
    start = minIndex - 1

    while start < end - 1:
        if (end - start) % 2 == 0:
            pivot = (end - start) // 2 + start
        else :
            pivot = (end - start + 1) // 2 + start

        if A[pivot] == B:
            maxIndex = pivot
            start = pivot
        if A[pivot] > B :
            end = pivot
        else:
            start = pivot
        if minIndex == 0 and maxIndex == 0 and A[0] != B :
            return [-1,-1]
    return[minIndex, maxIndex]


A =[ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
B= 1
print(
search_for_range(A, B)
)
def search_for_range(sorted_list, B):
    range = []
    start, end = 0, len(sorted_list)
    while start < end-1:
        if (end - start) % 2 == 0:
            pivot = start + (end - start)//2
        else :
            pivot = start + (end - start + 1) // 2
        if sorted_list[pivot] == B :
            range.append(pivot)
            if sorted_list[pivot-1] < B :
                start = pivot
            elif sorted_list[pivot + 1] > B:
                end = pivot
            else :
                start = pivot
        if sorted_list[pivot] > B :
            end = pivot
        else:
            start = pivot
    if len(range) == 0:
        return [0,0]
    return range
