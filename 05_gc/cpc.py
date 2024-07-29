#!/bin/env python

"""
Computing GC content
"""

import sys
import argparse
from typing import NamedTuple, TextIO, List, Tuple
from Bio import SeqIO


class Args(NamedTuple):
    """ Setting data structure types """
    file: TextIO


# -----------------------------------------------
def get_args() -> Args:
    """ Generating Args object """

    parser = argparse.ArgumentParser(
        description='Computein GC',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input is a file',
                        nargs='?',
                        default=sys.stdin)

    args = parser.parse_args()                      # parse arguments and stores in args variable
    return Args(args.file)


# ------------------------------------------------
#def main() -> None:
#    """ return class """
#
#    args = get_args()
#    seqs: List[Tuple[float, str] = []              # initialize emply list
#
#    for rec in SeqIO.parse(args.file, 'fasta'):     # iterate through each record
#        gc = 0                                      # initialize GC counter
#        for base in rec.seq.upper():                # iterate through each sequence
#            if base in ('G', 'C'):                  # check if base is G/C
#                gc += 1                             # increment gc counter
#        pct = (gc * 100) / len(rec.seq)             # compute GC %
#        seqs.append((pct, rec.id))                  # append tuple of GC and seqID
#
#    high = max(seqs)                                # take maximum value
#    print(f'{high[1]} {high[0]:0.3f}')              # print seq ID of highest value
#


# -------------------------------------------------
# S2
def main() -> None:
    """ return objects """

    args = get_args()
    seqs: List[Tuple[float, int]] = []
    
    for rec in SeqIO.parse(args.file, 'fasta'):
        seqs.append((find_gc(rec.seq), rec.id))
    
    high = max(seqs)
    print('Solution 2:')
    print(f'{high[1]} {high[0]:0.3f}')              # print seq ID of highest value


def find_gc(seq: str) -> float:
    """ Calculate GC content """

    if not seq:
        return 0.

    gc = 0
    for base in seq.upper():
        if base in 'GC':
            gc += 1

    return (gc * 100) / len(seq)
# --------------------------------------------------
if __name__ == '__main__':
    main()
