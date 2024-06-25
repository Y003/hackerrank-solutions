#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Attempt 1
def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)):
        newStr = "".join(c for ind, c in enumerate(s) if ind != i)
        if isPalindrome(newStr):
            return i
            
    return -1

def isPalindrome(s):
    
    return s == s[::-1]


# Attempt 2
def palindromeIndex(s):
    # Write your code here
    n = len(s)
    for i in range(n // 2 + 1):
        if s[i] != s[n-1-i]:
            if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
                return n-1-i
            else:
                return i

    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
