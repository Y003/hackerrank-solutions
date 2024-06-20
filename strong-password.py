#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


### First Attempt
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    minimunCharactersRequired = 0
    
    if not any(check(numbers, password)):
        minimunCharactersRequired += 1
    if not any(check(lower_case, password)):
        minimunCharactersRequired += 1
    if not any(check(upper_case, password)):
        minimunCharactersRequired += 1
    if not any(check(special_characters, password)):
        minimunCharactersRequired += 1
    
    if n < 6 and minimunCharactersRequired < (6 - n):
        minimunCharactersRequired = minimunCharactersRequired + (6 - n - minimunCharactersRequired)
    
    return minimunCharactersRequired

def check(s, arr):
    # returns a list of booleans
    result = [characters in s for characters in arr]
    return result

### Second Attempt
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    n_bool = 1
    l_bool = 1
    u_bool = 1
    s_bool = 1
    for c in password:
        if c in numbers: n_bool = 0
        elif c in lower_case: l_bool = 0
        elif c in upper_case: u_bool = 0
        elif c in special_characters: s_bool = 0
    return max(6-n, n_bool + l_bool + u_bool + s_bool)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
