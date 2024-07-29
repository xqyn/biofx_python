#!/bin/env python
"""
Date    : 2024-06-24
Purpose: tetranucleotide frequency (sol2)
"""

import argparse
import os
from typing import NamedTuple, Tuple


class Args(NamedTuple):
    """ Add args type """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get class args """

    parser = argparse.ArgumentParser(
        description='teranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
      )

    parser.add_argument(
        'dna',
        metavar='dna',
        help='Counting DNA sequence bases'
        )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Geting Args """
    args = get_args()

    print('{} {} {} {}'.format(*count(args.dna))) # The *counts syntax will expand the tuple into the four values needed by the format string; otherwise, the tuple would be interpreted as a single value.


# --------------------------------------------------
def count(dna: str) -> Tuple[int, int, int, int]:
    """" Count the number of A,T,G,C """

    count_a, count_t, count_c, count_g = 0, 0, 0, 0

    for base in dna:
        if base == "A":
            count_a += 1
        elif base == "T":
            count_t += 1
        elif base == "C":
            count_c += 1
        elif base == "G":
            count_g += 1
        else:
            pass
    return count_a, count_t, count_c, count_g


# --------------------------------------------------
def test_count() -> None:
    """ Test the count_dna function """

    assert count('A') == (1, 0, 0, 0)
    assert count('T') == (0, 1, 0, 0)
    assert count('C') == (0, 0, 1, 0)
    assert count('G') == (0, 0, 0, 1)
    assert count('') == (0, 0, 0, 0)    # unexpected value


# --------------------------------------------------
if __name__ == '__main__':
    main()
