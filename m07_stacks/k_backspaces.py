#2 K Backspaces
# The backspace key is broken. Every time the backspace key is pressed, instead
# of deleting the last (non-backspace) character, a '<' is entered.
#
# Given a string typed with the broken backspace key, write a program that
# outputs the intended string i.e what the keyboard output should be when
# the backspace key works properly.
#
# Input
# One line containing the string that was written in the text editor.
# Only contains lowercase letters from the English alphabet as well as
# the character '<'.
# '<' will not be the first character.
#
def k_backspace(test_str) :
    stack = []
    for char in test_str:
        if char == "<":
            stack.pop()
        else :
            stack.append(char)
    return ''.join(stack)

k_backspace("a<a<a<aa<<")

# Sample Output
# Input #1
# a<bc<
# Output #1
# b
#
#
# Input #2
# foss<<rritun
# Output #2
# forritun
#
#
# Input #3
# a<a<a<aa<<
# Output #3
#
# *empty string is intentional
