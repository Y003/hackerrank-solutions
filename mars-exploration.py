#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    if len(s) % 3 == 0:
        repeats = len(s) // 3
    else:
        repeats = ((len(s) - len(s) % 3) // 3) + 1
    originalMessage = "SOS" * repeats
    count = 0
    for i in range(len(s)):
        if s[i] != originalMessage[i]:
            count += 1
            
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
