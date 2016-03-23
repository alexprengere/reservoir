#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, division

from sys import stderr, stdin
from random import random


def build_reservoir(iterator, reservoir_size, verbose=False):
    if verbose:
        def log(s, *args):
            print(s.format(*args), file=stderr)
    else:
        def log(*_):
            pass

    res = []
    try:
        for n, item in enumerate(iterator, start=1):
            if len(res) < reservoir_size:
                log('> [p=1] Adding at index {0}: {1!r}', len(res), item)
                res.append(item)
            else:
                ind = int(random() * n)
                if ind < reservoir_size:
                    log('> [p={0}/{1}] Swap at index {2}: {3!r} -> {4!r}',
                        reservoir_size, n, ind, res[ind], item)
                    res[ind] = item
    except KeyboardInterrupt:
        print('\n! User interrupted the process, stopping now\n', file=stderr)

    return res


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('size', help="Reservoir size", type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    for row in build_reservoir(stdin,
                               reservoir_size=args.size,
                               verbose=args.verbose):
        print(row, end="")
