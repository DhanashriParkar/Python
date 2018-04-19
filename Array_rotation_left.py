# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:29:54 2018

@author: dhana
"""

def array_left_rotation(a, n, k):
    return a[k:]+a[:k]

n, k = map(int, input('Enter the size of array and number of rotations ').strip().split(' '))
a = list(map(int, input('Enter the array ').strip().split(' ')))
if k>=1 and k<=n:
    answer = array_left_rotation(a, n, k);
    print(*answer, sep=' ')
else:
    print('The value for number of rotations exceeds the elements in array')