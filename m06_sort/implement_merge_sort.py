# Given a list of unsorted numbers, sort them using the Merge Sort algorithm.
#
# Don't use the built-in sorted or list.sort() methods - the goal of this is
# to understand and implement the merge sort algorithm.
# def merge_sort(nums):

nums = [7, 5, 9, 3, 6, 0, 2, 4]

def merge_sort2(nums, first, last) :
    if first < last:
        # if (last - first) % 2 == 0:
        #     middle = (first + last) // 2
        # else :
        #     middle = (first + last + 1) // 2
        middle = (first+last) // 2
        merge_sort2(nums, first, middle)
        merge_sort2(nums, middle+1, last)
        merge(nums, first, middle, last)



def merge(nums, first, middle, last):
    left = nums[first:middle+1]
    right = nums[middle: last]
    l = r = 0
    for i in range(first, last):
        if nums[i] <= right[r]:
            nums[i] = left[l]
            l += 1
        else :
            nums[i] = right[r]
            r += 1
print(nums)
merge_sort2(nums, 0 , len(nums)-1)
print(nums)
