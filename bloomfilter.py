# -*- coding: utf-8 -*-
"""bloomfilter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UaxKaopW9kxmor_Dy-FOMh5kNKOpyLl4
"""

!pip install mmh3
!pip install numpy

import mmh3
import random
import math
import sympy
import numpy as np

"""
Run this on google colab for best results.
Input: I have inputed the strings and tested with one same value and one different.
Output: for same it is not certain but for different string it is certain that the string is not present in the bloom filter.
Dependencies: all the libraries in the import.

"""

m = int(input("length of Bitmap above 31: "))
if m < 31:
  m = int(input("length of Bitmap above 31: "))
bitarray = np.zeros(m)

def get_hash(key, p):
  if m > 42:
    p = m-p
  hashvalue = mmh3.hash(key, signed=False)% p
  return hashvalue

def bloom_filter(key):
  hash1 = get_hash(key, 7)
  hash2 = get_hash(key, 13)
  hash3 = get_hash(key, 23)
  hash4 = get_hash(key, 31)
  return hash1, hash2, hash3, hash4

names = 'ABCDE'

for c in names:
  bits = bloom_filter(c)
  for i in bits:
    bitarray[i] = 1
  
def working_bloom_filter(name):
  flag = 0
  bits = bloom_filter(name)
  for i in bits:
    if bitarray[i] == 0:
      flag = 1
  if flag == 1:
    return True
  else:
    return False

print("Returns True if fliter is 100% sure that the name is not present. It returns False if the filter is not sure if the name is present or not.")

print(working_bloom_filter('A'))
print(working_bloom_filter('R'))