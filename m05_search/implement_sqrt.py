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
def squareRoot(A):
    start = 0
    end = (A // 2) + 1
    if A == 1:
        return 1

    while start < end-1:
        print(start, "start")
        print(end, "end")
        pivot = (end - start) // 2 + start
        if pivot * pivot >= A:
            end = pivot
        if pivot * pivot <= A:
            start = pivot
    return start

print(squareRoot(1))
