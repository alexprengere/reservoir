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
from math import log as ln


def build_reservoir(data, R, verbose=False):
    if verbose:
        def log(s, *args):
            print(s.format(*args), file=stderr)
    else:
        def log(*_):
            pass

    threshold = 4 * R
    gap = 0
    res = []
    try:
        j, iterator = 0, iter(data)
        while True:
            j += 1
            item = next(iterator)
            if len(res) < R:
                log('> Adding at index {0}: {1!r}', len(res), item)
                res.append(item)

            elif j < threshold:
                k = int(random() * j)
                if k < R:
                    log('> [p={0}/{1}] Swap at index {2}: {3!r} replaces {4!r}', R, j, k, item, res[k])
                    res[k] = item
            else:
                gap = int(ln(random()) / ln(1 - R / j))
                for _ in range(gap):
                    item = next(iterator)
                j += gap
                k = int(random() * R)
                log('> Swap after gap {0} at index {1}: {2!r} replaces {3!r}', gap, k, item, res[k])
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
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    for row in build_reservoir(stdin,
                               R=args.size,
                               verbose=args.verbose):
        print(row, end="")
