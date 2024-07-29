#!/bin/env python
__description__="""
generating fi for seq
"""

import os
import textwrap
import argparse
from typing import NamedTuple

class Args(NamedTuple):
    """ Command for the Tuple """
    generations: int
    litter: int

# ---------------------------------
def get_args() -> Args:
    """ Command extract """
    
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(__description__),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('gen',
                        metavar='generations',
                        type=int,
                        help='Nunber of generations')

    parser.add_argument('litter',
                        metavar='litter',
                        type=int,
                        help='Size if liter per generation')

    args = parser.parse_args()

    if not 1 <= args.gen <= 40:
        parse.error("generations {args.gen} must between 1 and 40".format(args.gen))

    if not 1 <= args.litter <= 5:
        parse.error(f'litter "{args.litter}" must between 1 adn 5')

    return Args(args.gen, args.litter)


# ----------------------------------
def main() -> None:
    """ Return main """
    
    args = get_args()
    
    print("generations: {}".format(args.generations))
    print("litter: {}".format(args.litter))


# -----------------------------------
if __name__ == "__main__":
    main()
