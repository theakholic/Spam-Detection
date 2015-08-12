import string


def main():
    pass

if __name__ == '__main__':
    main()


def wc(file_path):
    """Count and return the number of words, lines and characters in a file."""
    nwords = nchars = nlines = 0

    with open(file_path) as f:
        for line in  f:
            nwords += len(line.split())
            nchars += len(line)
            nlines += 1

    return nwords, nchars, nlines



