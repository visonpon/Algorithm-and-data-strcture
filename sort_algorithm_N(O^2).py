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

def selectsort2(arr):
    for i in range(len(arr)):
        minposition=i#记录待交换元素的位置。
        for j in range(i+1,len(arr)):
            if arr[minposition]>arr[j]:
                minposition=j
        arr[i],arr[minposition]=arr[minposition],arr[i]#交换位置发生变化。
    print('select sorted1 array:', arr)
    return arr

def insertsort1(arr):
    for i in range(1,len(arr)):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i = i-1
    print('sorted1 array:',arr)
    return arr

#空间换时间，将交换操作的三次赋值减少为一次赋值。
def insertsort2(arr):
    for i in range(1,len(arr)):
        postion=i
        currentvalue = arr[i]
        while arr[postion-1]>currentvalue and postion>0:
            arr[postion] = arr[postion-1]
            postion = postion-1
        arr[postion] = currentvalue
    print('sorted2 array:', arr)
    return arr

max=5000
list=[randint(0,max) for x in range(max)]
#使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
alist=list[:]
blist=list[:]
clist=list[:]
dlist=list[:]

t0=timeit.Timer('selectsort1(alist)','from __main__ import selectsort1,alist')
print('选择排序1: %s s' %t0.timeit(number=1))

t1=timeit.Timer('selectsort2(blist)','from __main__ import selectsort2,blist')
print('选择排序2: %s s' %t1.timeit(number=1))

t2=timeit.Timer('insertsort1(clist)','from __main__ import insertsort1,clist')
print('插入排序: %s s' %t2.timeit(number=1))

t3=timeit.Timer('insertsort2(dlist)','from __main__ import insertsort2,dlist')
print('插入排序: %s s' %t3.timeit(number=1))
