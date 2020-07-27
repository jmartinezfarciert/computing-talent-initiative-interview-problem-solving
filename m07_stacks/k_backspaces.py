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
    output_list = []
    for i in range(len(test_str)):
        if test_str[i].isalpha():
            output_list.append(test_str[i])
        if test_str[i] == "<":
            output_list.pop()
    return ''.join(output_list)

k_backspaces("a<a<a<aa<<")

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
