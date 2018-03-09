#
# Find string sequences that match the following description:
#  "Now find adjacent four letter groups, first whispered, then shouted."
#

import regex as re

CHUNK_LENGTH = 4


def find_pair(source, chunk_length):
    # find lowercase strings of $chunk_length (whisper)
    matches = re.findall(r"[a-z]{%d}[A-Z]{%d}" % (chunk_length, chunk_length), source, overlapped=True)

    # find uppercase versions of the previous whispers (shout)
    for match in matches:
        print(match)


def load_data(path):
    """
    Load the data from the file.  Could get really fancy and load it from the webpage.
    """
    with open(path, 'r') as f:
        rows = [l.strip() for l in f.readlines()]
    return rows


def load_row_wise(rows):
    """
    Join all the rows into one string left to right, top to bottom.
    """
    return ''.join(rows)


def load_col_wise(rows):
    """
    Join all the rows into one string top to bottom, left to right,
    """
    num_rows = len(rows)
    num_cols = len(rows[0])

    col_wise = ''
    for column in range(num_cols):
        for row in range(num_rows):
            col_wise += rows[row][column]
    return col_wise


if __name__ == '__main__':
    rows = load_data('./adjacent.dat')

    # this yielded a bunch.  probably not right.
    # col_wise = load_col_wise(rows)
    # find_pair(col_wise, CHUNK_LENGTH)

    # this yielded 1.  seems sensible.
    row_wise = load_row_wise(rows)
    find_pair(row_wise, CHUNK_LENGTH)

    # yields pqvsTNSQ
