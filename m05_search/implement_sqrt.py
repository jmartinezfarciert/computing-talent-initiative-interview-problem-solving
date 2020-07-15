# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Do not use any built square root functions.
#
# Example 1:
# Input: 4
# Output: 2
#
#
# Example 2:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
def squareRoot(num):
    start = 0
    end = (num // 2) + 1

    while start < end-1:
        print(start, "start")
        print(end, "end")
        if (end - start) % 2 == 0:
            pivot = int((end - start) / 2) + start
        else :
            pivot = int((end - start + 1) / 2) + start
        if pivot * pivot > num:
            end = pivot
        if pivot * pivot < num:
            start = pivot
        if pivot * pivot == num :
            start = pivot
            end = pivot
    return start


sampleInput = 16
print(squareRoot(sampleInput))
