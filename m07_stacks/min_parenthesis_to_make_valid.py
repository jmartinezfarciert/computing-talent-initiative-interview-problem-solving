#
# Given a string S of '(' and ')' parentheses, we add the minimum number of
# parentheses ( '(' or ')', and in any positions ) so that the resulting
# parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or It can be written as (A), where A is a valid string.
#
# Given a parentheses string, return the minimum number of
# parentheses we must add to make the resulting string valid.
#
# Input
# S.length <= 1000
# S only consists of '(' and ')' characters.
#
def minAddToMakeValid(S):
    stack = []
    for ch in S :
        if ch == ")" and "(" in stack:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)

sampleInput = '()'
print(minAddToMakeValid(sampleInput))

# Sample Output
# input#1
# ())
# output#1
# 1
#
# input#2
# (((
# output#2
# 3
#
# input#3
# ()
# output#3
# 0
#
#
# input#4
# ()))((
# output#4
# 4
