# Given a long text string, count the number of occurrences of each word.
# Ignore case. Assume the boundary of a word is whitespace - a " ", or a
# line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !.
# Assume hyphens are part of a word - "two-year-old" and "two year old" are one
# word, and three different words, respectively.
#
# Return the word counts as a string formatted with line breaks, in
# alphanumeric order.

def count_words(text):
    words = text.lower().split()
    counts = {}
    output = ""
    for word in words:
        word = word.replace(",", "").replace(".", "")
        if word not in counts:
            counts[word] = 1
        else:
            counts[word]+= 1
    for word, count in counts.items():
        output += word + " " + str(count) + "\n"
    return output
# {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
input = "I do not like green eggs and ham, I do not like them, Sam-I-Am"
count_words(input)
# Output:
# i 2
# do 2
# not 2
# like 2
# green 1
# eggs 1
# and 1
# ham 1
# them 1
# sam-i-am 1
