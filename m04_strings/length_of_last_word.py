# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
# Given s = "Hello World",
# return 5 as length("World") = 5.
#
# Please make sure you try to solve this problem without using library
# functions. Make sure you only traverse the string once.
# @param A : string
# @return an integer
def length_of_last_word(A):
  count = 0
  A = A.strip()
  print(A)

  if len(A) == 0 or " " not in A:
      return 0

  for i in reversed(A):
      if i.isalnum():
          count += 1
      else:
          break

  return count
print(
length_of_last_word("World")
)

# Using Library functions
def length_of_last_word(words):
    words = words.strip()
    words = words.split()
    if len(words) == 0:
        return 0
    last_word = words[len(words)-1]
    return len(last_word)
