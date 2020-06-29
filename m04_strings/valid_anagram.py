def valid_anagram(s, t):
    # contains same characters in varying order
    return sorted(s) == sorted(t)

print(
valid_anagram("bsoy", "byo")
)
