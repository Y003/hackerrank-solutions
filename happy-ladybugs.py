#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    char_count = Counter(b)
    # If there's any ladybug that appears exactly once, it can't be happy
    for char, count in char_count.items():
        if char != '_' and count == 1:
            return "NO"
    
    # If there are no empty spaces, check if the ladybugs are already happy
    if '_' not in char_count:
        for i in range(1, len(b) - 1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return "NO"
    
    # If there are empty spaces and no isolated ladybugs, return YES
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
