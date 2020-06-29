# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
# import string
# def isPalindrome(s):
#     s = s.lower() #ignoring case
#     # s = s.translate(None, string.punctuation)
#     s.translate(str.maketrans('', '', string.punctuation))
#     s = s.replace(" ", "")
#     return s == s[::-1]
#

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(A):
        s = A.lower() #ignoring case
        s = s.replace(" ", "")
        clean_string = ""
        for ch in s:
            if ch.isalnum():
                clean_string = clean_string + ch
        return int(clean_string == clean_string[::-1])

    print(
    isPalindrome("1a2")
    )
