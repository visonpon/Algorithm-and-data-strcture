# -*- coding: utf-8 -*-
from random import randint
import timeit

def selectsort1(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    print('select sorted1 array:',arr)
    return arr
