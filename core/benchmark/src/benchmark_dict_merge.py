#!/usr/bin/env python3

import timeit


left = {
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 1,
    'e': 1,
    'f': 1,
    'g': 1,
    'h': 1,
    'i': 1,
    'j': 1,
}

right = {
    'a': 1,
    'z': 1,
    'c': 1,
    'y': 1,
    'e': 1,
    'x': 1,
    'g': 1,
    'w': 1,
    'i': 1,
    'v': 1,
}

result = None


def benchmark_star_merge():
    result = { **left, **right }

def benchmark_or_merge():
    result = left | right


#print(timeit.timeit(stmt="benchmark_or_merge()", setup="from __main__ import benchmark_or_merge"))
#print(timeit.timeit(stmt="benchmark_star_merge()", setup="from __main__ import benchmark_star_merge"))
print(timeit.timeit(stmt="result = { **left, **right }", setup="from __main__ import left, right, result"))
print(timeit.timeit(stmt="result = left | right", setup="from __main__ import left, right, result"))

