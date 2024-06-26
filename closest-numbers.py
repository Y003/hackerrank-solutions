#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    minDiff = arr[1] - arr[0]
    finArray = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == minDiff:
            finArray.append(arr[i])
            finArray.append(arr[i+1])
        elif arr[i+1] - arr[i] < minDiff:
            minDiff = arr[i+1] - arr[i]
            finArray.clear()
            finArray.append(arr[i])
            finArray.append(arr[i+1])
    
    return finArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
