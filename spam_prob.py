import heapq
from word_freq import tokenize
import spamicity
import PythonLabs.SpamLab
import string

def IQ(p):
    """Return Interestingness Quotient of the proobability which is |0.5 - p|"""
    return abs(0.5 - p)

p1 =[]
p2 = []

def combine_probs(priority_queue):
    qu = PythonLabs.SpamLab.WordQueue(15)
    for p,w in priority_queue:
        qu.insert(w,p)
    return PythonLabs.SpamLab.combined_probability(qu)


def prob_spam(email_file_path):
    q = []
    p_good,p_bad = spamicity.load_dicts()

    assert p_good['looking'] == 0.0530

    with open(email_file_path) as f:
        #read each line, tokenize, add to queue with spamicity
        for line in f:
            words = tokenize(line)
            for word in words:
                prob = spamicity.conditional_spam(word,p_good,p_bad)
                #print('word: {} prob: {}'.format(word, prob))
                if prob is not None:
                    p1.append((word, prob))
                    heapq.heappush(q,(prob, words))

    return combine_probs(q)

def pspam(fn):
    queue = PythonLabs.SpamLab.WordQueue(15)
    p_good, p_bad = spamicity.load_dicts()
    for line in open(fn):
        for word in tokenize(line):
            p = spamicity.conditional_spam(word, p_good, p_bad)
            if p is not None:
                p2.append((word, p))
                queue.insert(word, p)

    return PythonLabs.SpamLab.combined_probability(queue)

def main():
    p_good,p_bad = spamicity.load_dicts()



if __name__ == '__main__':
    main()
