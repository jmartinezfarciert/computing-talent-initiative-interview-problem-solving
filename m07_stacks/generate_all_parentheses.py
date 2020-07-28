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

#Liz Howards Solution
def valid(A):
  # helper function, returns whether or not a bracket is an opening bracket
  def openBracket(bracket):
    return bracket in "{[("
  # helper function, returns whether or not two brackets are of the same type
  def sameType(bracket1, bracket2):
    if bracket1 in "{}": return bracket2 in "{}"
    if bracket1 in "()": return bracket2 in "()"
    if bracket1 in "[]": return bracket2 in "[]"

  # keep track of brackets we've come across using a stack
  stack = []
  for bracket in A:
    # push open brackets onto the stack, only popping them once we find a closing bracket
    if openBracket(bracket):
      stack.append(bracket)
    # if this bracket wasn't an opening bracket, and there are no open brackets on the stack, then we've come across an out-of-place closing bracket
    elif len(stack) == 0:
      return 0
    # if the closing bracket we've come across is of the same type as the opening bracket on the top of the stack, then this is a valid pair of A
    elif sameType(stack[-1], bracket):
      stack.pop()
    # otherwise, the brackets are mismatched and this is an invalid string
    else:
      return 0

  # if there are no open brackets left hanging on the stack, then all brackets have a valid partner
  if len(stack) == 0:
    return 1
  else:
    return 0
