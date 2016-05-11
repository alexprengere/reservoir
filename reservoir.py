#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python implementation for
http://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/
"""

from __future__ import with_statement, print_function, division
try:
    range = xrange
except NameError:
    pass

from sys import stderr, stdin
from random import random
from math import log


def build_reservoir(data, R, threshold=None, verbose=False):
    if verbose:
        def p(s, *args):
            print(s.format(*args), file=stderr)
    else:
        def p(*_):
            pass

    if threshold is None:
        threshold = 4 * R
    res = []
    try:
        j = 0
        iterator = iter(data)
        while True:
            j += 1
            item = next(iterator)
            if len(res) < R:
                p('> Adding element nb {0}: {1!r}', len(res), item)
                res.append(item)

            elif j < threshold:
                k = int(random() * j)
                if k < R:
                    p('> [p={0}/{1:>9}] Swap element nb {2:>5}: {3!r} replaces {4!r}', R, j, k, item, res[k])
                    res[k] = item
            else:
                gap = int(log(random()) / log(1 - R / j))
                j += gap
                for _ in range(gap):
                    item = next(iterator)
                k = int(random() * R)
                p('> After skipping {0:>9} lines, swap element nb {1:>5}: {2!r} replaces {3!r}', gap, k, item, res[k])
                res[k] = item

    except KeyboardInterrupt:
        print('\n! User interrupted the process, stopping now\n', file=stderr)
    except StopIteration:
        pass

    return res


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('size', help="Reservoir size", type=int)
    parser.add_argument('-t', '--threshold',
                        help=('threshold to start using gaps, default '
                              ' is 4 times the reservoir size'),
                        type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    for row in build_reservoir(stdin,
                               R=args.size,
                               threshold=args.threshold,
                               verbose=args.verbose):
        print(row, end="")
