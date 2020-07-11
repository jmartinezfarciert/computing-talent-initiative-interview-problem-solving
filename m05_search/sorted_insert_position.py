# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
# Examples:
#
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4 --> int((end - start) / 2) + start caused a problem
# [1,3,5,6], 0 → 0

def find_index(sorted_list, target):
    start = -1
    end = len(sorted_list)
    # target_index = 0
    test_index = 0
    while start < end-1:
        # test_index = int((end - start) / 2) + start
        if (end - start) % 2 == 0 :
            test_index = int((end - start) / 2) + start
        else:
            test_index = int((end - start + 1) /2) + start

        if sorted_list[test_index] <= target:
            start = test_index
        if sorted_list[test_index] >= target:
            end = test_index
    print(test_index)
    if sorted_list[test_index] >= target:
        return test_index
    else :
        return test_index + 1


print(
find_index([1,3,5,6],2)
)

#Liz Howard's solution
def find_index(sorted_list, target):
    start, end = 0, len(sorted_list)
    while start < end:
        pivot = start + (end - start) // 2
        if sorted_list[pivot] < target:
            start = pivot + 1
        else:
            end = pivot
    return start
