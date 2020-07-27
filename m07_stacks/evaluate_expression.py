
# Reverse polish notation is a postfix notation for mathematical expressions.
# For example, the infix expression (1 + 2) / 3 would become 1 2 + 3 /

# https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# Task:
# Given a mathematical expression in reverse polish notation, represented
# by an array of strings, find the answer to this expression. Operators consist
# only of +, -, *, /, and all numbers are integer values. When performing a
# division on two numbers, use python's integer division operator (//).
# Your output should be a single integer, which is the value of the expression
# when evaluated. Each expression is guaranteed to be valid.
#
def evaluate_expression(expression):
    stack = []
    #loop over every element in the list
    for element in expression :
        # if the element is an operator:
        if element in ["+", "-", "/", "*"]:
            # perform an operation on the preceding two numbers
            b = int(stack.pop())
            a = int(stack.pop())
            if element == "+":
                x = a + b
            if element == "-":
                x = a - b
            if element == "*":
                x = a * b
            if element == "/":
                x = a // b
            stack.append(x)
        else :
            stack.append(element)
    return stack.pop()

evaluate_expression(["3", "4", "+", "5", "-"])
# Example 1:
# expression = ["3", "4", "+", "5", "-"]
# print(evaluate_expression(expression))
# >> 2
#
# Example 2:
# expression = ["3", "4", "/", "5", "*"]
# print(evaluate_expression(expression))
# >> 0
#
# Explanation 1:
# "3 4 + 5 -" is equivalent to the infix expression "3 + 4 - 5"
# The answer to this expression is 2.
#
# Explanation 2:
# "3 4 / 5 *" is equivalent to the infix expression "3 / 4 * 5"
# Since we are using integer division, 3 / 4 = 0, and 0 * 5 = 0.
# The answer to this expression is 0.
