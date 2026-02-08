from typing import SupportsInt
from types import NoneType

def length_of_longest_substring(s: str) -> int:
    char_hash = dict()
    start = 0
    max_length = 0

    for indx, val in enumerate(s):
        if val in char_hash and char_hash[val] >= start:
            start = char_hash[val] + 1
        
        char_hash[val] = indx
        max_length = max(max_length, indx - start + 1)

    return max_length
