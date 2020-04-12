# -*- coding: utf-8 -*-
# authored by dp 2020/04/12

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


def insertsort10(arr):
    for i in range(1,len(arr)):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i = i-1
    print('sorted10 array:',arr)
    return arr

def insertsort11(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break #break比while时间效率更高
    print('sorted11 array:',arr)
    return arr
#空间换时间，将交换操作的三次赋值减少为一次赋值。
def insertsort20(arr):
    for i in range(1,len(arr)):
        postion=i
        currentvalue = arr[i]
        while arr[postion-1]>currentvalue and postion>0:
            arr[postion] = arr[postion-1]
            postion = postion-1
        arr[postion] = currentvalue
    print('sorted20 array:', arr)
    return arr


def insertsort21(arr):
    for i in range(1,len(arr)):
        postion=i
        currentvalue = arr[i]
        for j in range(i,0,-1):
            if arr[postion-1]>currentvalue:
                arr[postion] = arr[postion-1]
                postion = postion-1
            else:
                break
        arr[postion] = currentvalue
    print('sorted21 array:', arr)
    return arr

max=5000
list=[randint(0,max) for x in range(max)]
#使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
alist=list[:]
blist=list[:]
clist=list[:]
dlist=list[:]
elist=list[:]
flist=list[:]


t00=timeit.Timer('selectsort1(alist)','from __main__ import selectsort1,alist')
print('选择排序1: %s s' %t00.timeit(number=1))

t01=timeit.Timer('selectsort2(blist)','from __main__ import selectsort2,blist')
print('选择排序2: %s s' %t01.timeit(number=1))


t10=timeit.Timer('insertsort10(clist)','from __main__ import insertsort10,clist')
print('插入排序10: %s s' %t10.timeit(number=1))

t11=timeit.Timer('insertsort11(dlist)','from __main__ import insertsort11,dlist')
print('插入排序11: %s s' %t11.timeit(number=1))

t20=timeit.Timer('insertsort20(elist)','from __main__ import insertsort20,elist')
print('插入排序20: %s s' %t20.timeit(number=1))


t21=timeit.Timer('insertsort21(flist)','from __main__ import insertsort21,flist')
print('插入排序21: %s s' %t21.timeit(number=1))

