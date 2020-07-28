# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all
# valid but "(]" and "([)]" are not.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
#
# Original Site:  https://www.interviewbit.com/problems/generate-all-parentheses/
#
def valid(A):
    stack = []
    for ch in A:
        if len(stack) == 0:
            stack.append(ch)
            continue
        if ch == ")" and stack.pop() == "(":
            continue
        if ch == "]" and stack.pop() == "[":
            continue
        if ch == "}" and stack.pop() == "{":
            continue
        else :
            stack.append(ch)
    return len(stack) == 0

print(
valid("()[]{}")
)
