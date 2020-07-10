#!/bin/python3

import math
import os
import random
import re
import sys

'''
Understand:
    if I am give and odd number print the word weird
    if I am given and even number with in the range of 2 to 5 print Not weird
    if I am given an even number with in the range of 6 to 20 print weird
    if I am given an even number larger than 20 print not weird

Planning:
    -figure out how to determine if it is even or odd and what the number is? 
    If N % 2 != 0:
        print(weird)
    elif N % 2 == 0 and 2 >= N <= 5:
        print(Not Wierd)
    elif N % 2 == 0 and 6 >= N <= 20:
        print(Wierd)
    elif N % 2 == 0 and N > 20
        print(Not Wierd)    
'''

  

if __name__ == '__main__':
    N = int(input())

if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and 2 <= N <= 5:
    # print(Not Weird)
    print("Not Weird")

elif N % 2 == 0 and 6 <= N <= 20:
    print("Weird")

elif N % 2 == 0 and N > 20:
    print("Not Weird") 
