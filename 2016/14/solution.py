"""
Advent of Code 2016
Day 14: One-Time Pad
https://adventofcode.com/2016/day/14
"""
from functools import lru_cache
from hashlib import md5
from re import compile, search as regex_search


def read_input_file():
    return open("input.txt", "r").read().strip()


@lru_cache(maxsize=None)
def get_md5(s):
    return md5(s.encode("ascii")).hexdigest()


@lru_cache(maxsize=None)
def get_long_md5(s):
    for _ in range(2017):
        s = md5(s.encode("ascii")).hexdigest()
    return s


def index_of_64th_pad_key(salt_text, long=False):
    fn = get_long_md5 if long else get_md5
    i, j = 0, 0
    salt = salt_text + "{}"
    regex = compile(r"([abcdef0-9])\1{2}")
    while True:
        g = regex_search(regex, fn(salt.format(i)))
        if g:
            check = g.group()[0] * 5
            if any(check in fn(salt.format(j)) for j in range(i + 1, i + 1001)):
                j += 1
                if j == 64:
                    return i
        i += 1


if __name__ == "__main__":
    input_text = read_input_file()
    print(index_of_64th_pad_key(input_text))
    print(index_of_64th_pad_key(input_text, long=True))
