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
    start = 0
    end = len(sorted_list)-1
    target_index = 0
    while start < end-1 :
        # test_index = int((end - start) / 2) + start
        if (end - start) % 2 == 0 :
            test_index = int((end - start) / 2) + start
        else:
            test_index = int((end - start + 1) /2) + start

        if sorted_list[test_index] < target:
            start = test_index
            target_index = test_index + 1
        if sorted_list[test_index] > target:
            end = test_index
            target_index = test_index
        if sorted_list[test_index] == target :
            target_index = test_index
            start = target_index
            end = target_index
    if target_index == len(sorted_list)-1 and sorted_list[target_index] != target:
        target_index = len(sorted_list)
    if target_index == 1 and sorted_list[target_index] != target:
        target_index = 0
    return target_index

print(
find_index([1,3,5,6],1)
)
