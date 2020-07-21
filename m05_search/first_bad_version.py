# You are a product manager and currently leading a team to develop a new
# product.
#  Unfortunately, the latest version of your product fails the quality check.
#  Since each version is developed based on the previous version, all the
 # versions
#  after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.
#
# Example:
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.
# Although you cannot see it, imagine there is a function called isBadVersion already defined.
# the automatic tests will account for it
# here is an example implementation, although the tests will have a different actual value
# the first bad version won't always be 7, but the other function will behave similarly

def isBadVersion(version):
  return version > 7

def firstBadVersion(last_version, isBadVersion):
    start = 1
    while start < last_version:
        testVersion = start + ((last_version - start) // 2)
        if isBadVersion(testVersion):
            last_version = testVersion
        else :
            start = testVersion + 1

    return start


# Liz Howard's model solution
def firstBadVersion(last_version, isBadVersion):
  end = last_version
  start = 1

  while start < end:
    pivot = start + ((end - start) // 2)
    if isBadVersion(pivot):
      end = pivot
    else:
      start = pivot + 1
  return start
