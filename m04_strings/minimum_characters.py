# Minimum Characters required to make a String Palindromic
# You are given a string. The only operation allowed is to insert characters
# in the beginning of the string. Return the number of characters that are
# needed to be inserted to make the string a palindrome string
#
#

# def minimumCharacters(s):
#     counter = 0
#     for i in range(int(len(s)/2)):
#         if s[i] not in s[i+1:len(s)-i]:
#             counter += 1
#     return counter

# #go fucking backwards
# # 0 1 2 3 4 5 6 7 8
# # A A C E C A A A A
# #-9-8-7-6-5-4-3-2-1
# def minimumCharacters(s):
#     for i in range(-1, -8):
#         print(i)
#         print("s[i]", s[i])
#         print("s[i + len(s)]", s[i + len(s)])
#         # if s[i] != s[i + len(s)]:


# def minimumCharacters(s):
#     minimumCharacters = 0
#
#     for i in range(len(s)):
#         sub_string = s[:len(s)-i]
#         backwards_sub_string = sub_string[::-1]
#         if sub_string == backwards_sub_string:
#             break
#         minimumCharacters += 1
#     return minimumCharacters

def minimumCharacters(A):
    sub_string = A[:]
    while True:
        sub_string = sub_string[:sub_string.rfind(A[0])+1]
        if sub_string == sub_string[::-1] : # backwards
            return len(A) - len(sub_string)
        sub_string = sub_string[:sub_string.rfind(A[0])]

# Examples:
# Input: ABC
print(
minimumCharacters('ABC')
)
# Output: 2
# Input: AACECAAAA
# Output: 2
