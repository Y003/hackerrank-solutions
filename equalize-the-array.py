#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    freqArr = countFrequency(arr)
    maxFreq = max(list(freqArr.values()))
    
    return len(arr) - maxFreq

    
def countFrequency(arr):
    freqArr = {}
    for i in range(len(arr)):
        if arr[i] in freqArr:
            freqArr[arr[i]] += 1
        else:
            freqArr[arr[i]] = 1
    
    return freqArr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
