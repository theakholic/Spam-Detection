import wc


PATH_TO_GOOD = r'F:/Python/Text_Files/good.txt'
PATH_TO_BAD = r'F:/Python/Text_Files/bad.txt'


def spamicity(word, p_good, p_bad):
    """
    Return the probability that a mail is spam given that word is present in it.
    p_good is a dict with p_good[w] = P(w|good)
    p_bad is a dict with p_bad[w] = P(w|spam)

    spamicity(f) = P(spam|word) = P(word|spam)*P(spam)/(P(word|spam)*P(spam) + P(word|good)*P(good)) [BY BAYES THEOREM]
    We assume spam and non-spam mails can occur with equal probability, so P(spam) = P(good) = 1/2.

    Note: if word is not in both p_good and p_bad return None.

    >>> spamicity(word='money', p_good={'money' : 0.0164}, p_bad={'money' : 0.127})
    0.8856345885634589

    """
    if word in p_good and word in p_bad: #neither of probabilities zero
        return p_bad[word]/(p_good[word] + p_bad[word])

    return None


def read_file(path_to_file):
    """
    Read a file containing lines of "float string" representing the
    P(word|spam) and P(word|good) for each word and return a dict that
    captures in data.
    """
    d = {}
    with open(path_to_file) as f:
        try:
            for line in f:
                t = line.split()
                if len(t) != 2:
                    raise ValueError('The file is not apt for this program. The file must have "float string" lines only.')
                d[t[1]] = float(t[0])
        except ValueError as e:
            print(e)
            return None


    return d

def load_dicts():
    p_bad = read_file(PATH_TO_BAD)
    p_good = read_file(PATH_TO_GOOD)
    return p_bad, p_good

def main():
    print('Loading data...')
    p_bad, p_good = load_dicts()
    print('Loaded.')


if __name__ == '__main__':
    main()
