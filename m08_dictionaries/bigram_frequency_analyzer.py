
def bigram_frequency_analyzer(text):
# Given a long string of text, do not ignore punctuation.
# Break the text into individual words.
    words = text.split()

    dict = {}
    # Then, for every two words, count the frequency of words that come after
    output = ""
    for i in range(len(words)-2):
        word_pair = words[i]+ " "+words[i+1]
        if word_pair in dict:
            dict[word_pair].append(words[i+2])
        else:
            dict[word_pair] = [words[i+2]]
    for word_pair, words in dict.items():
        word_set = set(words)
        output += word_pair + " : "
        for word in word_set:
            count = dict[word_pair].count(word)
            output += word + " (" + str(count) + ") "
        output += "\n"
    return output

ex = "I do not like green eggs and ham, I do not like them, Sam-I-Am! I do not like them with a fox, I do not like them in a box. I do not like them here or there, I do not like them anywhere! I do not like them, Sam-I-Am, I do not like green eggs and ham!"
print(
bigram_frequency_analyzer(ex)
)
# those two words by storing them
# as a list of occurrences. Return a string (with line breaks) that shows
# the frequency of those words.
