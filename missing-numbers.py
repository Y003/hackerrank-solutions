#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

# ROOKIE APPROACH

def missingNumbers(arr, brr):
    # Write your code here
    arrFreq = countFrequency(arr)
    brrFreq = countFrequency(brr)
    output = []
    for key in brrFreq:
        if key not in arrFreq:
            output.append(key)
        elif key in arrFreq and brrFreq[key] != arrFreq[key]:
            output.append(key)
    
    output.sort()
    
    return output

def countFrequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
            
    return freq


# PRO APPROACH

def missingNumbers(arr, brr):
    # Write your code here
    return sorted([n for n in Counter(brr) - Counter(arr)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
