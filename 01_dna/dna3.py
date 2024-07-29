#!/bin/env python

"""
2024-06-26
"""

import argparse
import os
from typing import NamedTuple, Tuple


class Args(NamedTuple):
    """ Add new class Args """
    dna: str


# --------------------------------------------------
def get_args() -> Args:  # return class Args
    """ Get dna seq """

    parser = argparse.ArgumentParser(
            description='tetranucleotide frequency',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )

    parser.add_argument(
            'dna',
            metavar='dna',
            help='counting DNA sequence bases'
            )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Getting args """
    args = get_args()

    print('{} {} {} {}'.format(*(count(args.dna))))


# --------------------------------------------------
def count(dna: str) -> Tuple[int, int, int, int]:
    """ Geting DNA string """

    counts = {}
    for base in dna:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return (counts.get('A', 0),
            counts.get('T', 0),
            counts.get('C', 0),
            counts.get('G', 0))


# --------------------------------------------------
if __name__ == '__main__':
    main()
