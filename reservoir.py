#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, division

import logging
from random import random


def reservoir(iterator, K):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len(result) < K:
            result.append(item)
            logging.warn('Adding %r to unfilled reservoir', item)
        else:
            ind = int(random() * N)
            if ind < K:
                logging.warn('[Probability %s/%s] Replacing item at index %s with %r',
                             K, N, ind, item)
                result[ind] = item

    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('You must provide the reservoir length')
        exit(1)

    for row in reservoir(sys.stdin, K=int(sys.argv[1])):
        print(row, end="")
