# Implement atoi which converts a string to an integer.
#
# Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral
# number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or it
# contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered as whitespace character.
#
def atoi(a):
    INT_MIN = -2147483648
    INT_MAX = 2147483647 # input =  "2147483648"
    a = a.strip()
    integer_string = ""
    if len(a)== 0 :
        return 0
    if a[0] == "+" or a[0] == "-" :
        integer_string += a[0]
    elif not a[0].isnumeric():
        return 0
    for i in range(len(integer_string), len(a)):
        if not a[i].isnumeric():
            break
        integer_string += a[i]
    if len(integer_string) == 1 and not integer_string.isnumeric(): # input =  "+-2", "+"
        return 0
    else :
        integer = int(integer_string)
        if integer > INT_MAX:
            return INT_MAX
        if integer < INT_MIN:
            return INT_MIN
        return integer

input =  "2147483648"
print(
atoi(input)
)
# Liz Howards Solution
def atoi(a):
    if not len(input_string):
        return 0

    sign = 1
    if input_string[0] == "-":
        sign = -1
        input_string = input_string[1:]
    if input_string[0] == "+"
        input_string = input_string[1:]

    a.strip()
    final_number = " "
    for character in input_string:
    if character.isnumeric():
        final_number += character
    else:
        break
    if len(final_number) == 0:
        return 0
    num = int(final_number) * sign
    if num > 2 ** 32 or num < ((2**32) * -1):
        return 2147483648 * sign
    else:
        return num
