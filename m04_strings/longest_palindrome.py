# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

def longest_palindrome(input_string):
    i = 0
    longest_palindrome = ""
    while i < len(input_string)-1:
        substring = input_string[i: input_string.rfind(input_string[i])+1].strip() # find word that ends with the first char and strip it of white space to test for palindrome
        if len(substring) > 1 and substring == substring[::-1] and len(substring) > len(longest_palindrome):
            longest_palindrome = substring
        i += 1
    return(longest_palindrome)

print(
longest_palindrome("i want to be a racecar driver")
)

def longest_palindrome(input_string):
    longest_palindrome = ""
    reversed_string = input_string[::-1]
    for i in range(len(input_string)):
        if input_string[i] == reversed_string[i]:
            longest_palindrome += input_string[i]
    return longest_palindrome
