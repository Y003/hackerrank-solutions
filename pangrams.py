#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Create a set 'alphabet' containing all lowercase letters using 'string.ascii_lowercase'.
    alphabets = set(string.ascii_lowercase)
    if set(s.lower()) >= alphabets:
        return "pangram"
    else:
        return "not pangram"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
