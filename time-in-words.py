#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


# 1st Approach
# ===========================
# def timeInWords(h, m):
#     # Write your code here
#     wordDictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'ninteen', 20: 'twenty'}
    
#     if m == 0:
#         return wordDictionary[h] + " o' clock"
#     elif m == 30:
#         return "half past " + wordDictionary[h]
#     elif m == 15:
#         return "quarter past " + wordDictionary[h]
#     elif m == 45:
#         return "quarter to " + wordDictionary[h + 1]
#     elif m == 1:
#         return wordDictionary[m] + " minute past " + wordDictionary[h]
#     elif m == 59:
#         return wordDictionary[m] + " minute to " + wordDictionary[h + 1]
#     elif m > 1 and m < 21:
#         return wordDictionary[m] + " minutes past " + wordDictionary[h]
#     elif m > 20 and m < 30:
#         return "twenty " + wordDictionary[m % 10] + " minutes past " + wordDictionary[h]
#     elif m > 30 and m < 40:
#         return "twenty " + wordDictionary[(60 - m) % 10] + " minutes to " + wordDictionary[h + 1]
#     else:
#         return wordDictionary[(60 - m)] + " minutes to " + wordDictionary[h + 1]
        
                
# 2nd Approach
# ===========================
def timeInWords(h, m):
    res = ''
    numbers = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    minute = 'minute'
    
    if m != 1:
        minute += 's'
        
    if m == 0:
        res = numbers[h] + " o' clock"
    elif m == 30:
        res = "half past " + numbers[h]
    elif m == 15:
        res = "quarter past " + numbers[h]
    elif m == 45:
        res = "quarter to " + numbers[h + 1]
    elif m < 20:
        res = numbers[m] + ' ' + minute + ' past ' + numbers[h]
    elif m < 30:
        res = numbers[-1] + ' ' + numbers[int(m%10)] + ' ' + minute + ' past ' + numbers[h]
    elif m > 45:
        res = numbers[60 - m] + ' ' + minute + ' to ' + numbers[h + 1]
    elif m > 30:
        res = numbers[-1] + ' ' + numbers[int(m%10)] + ' ' + minute + ' to ' + numbers[h + 1]
    
    return res.replace('  ', ' ')  
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
