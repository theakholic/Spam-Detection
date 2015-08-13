import string
def word_freq(s):
    """Return dict of word frequences in the string."""
    freq = {}

    t = tokenize(s)
    for word in t:
        freq.setdefault(word,0)
        freq[word] += 1

    return freq

def tokenize(line):
    """Split line into list of lower case words with punctuations removed."""
    t = []
    for word in line.split():
        t.append(word.strip(string.punctuation).lower())

    return t

def word_freq_in_file(file_name):
    freq = {}

    with open(file_name) as f:
        for line in f:
            d = word_freq(line)
            freq.update(d)

    return freq