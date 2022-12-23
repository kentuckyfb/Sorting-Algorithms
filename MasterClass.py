# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 23:49:48 2022

@author: aiamini
"""

import sys

sys.setrecursionlimit(100000)

class masterClass:
  
  #function to find the correct index of the pivot and put it there
  def GetPivotIndex(arr, low, high):
    i = low             # i to keep track of elements greater than pivot
    j = high-1          # j to keep track of elements lesser than pivot
    pivot = arr[high]   # take last element in list as pivot

    while i < j:
      #while loop to find an element greater than the pivot in the array goin from beggning to end
      while i < high and arr[i] < pivot:
        i += 1

      #while loop to find an element lesser than pivot going from end to beggning of the array
      while j > low and arr[j] >= pivot:
        j -= 1

      #if i and j have crossed each other
      if i < j:
        arr[i], arr[j] = arr[j], arr[i]

    #switch i index with pivot when while loop stops
    if arr[i] > pivot:
      arr[i], arr[high] = arr[high], arr[i]
    #return i(pivots proper position) in array
    return i

  #recursive function for quicksort 
  def quickSort (arr, low, high ):
    if(low < high):
      pi = masterClass.GetPivotIndex(arr, low, high)  #divides the list around the index of the pivot element 
      masterClass.quickSort(arr, low , pi -1)     # from first to partition index 
      masterClass.quickSort(arr, pi+1 , high)     # from partition index to last


  #getting min index of an array using recursion
  def minIndex( arr , index , l ):
    #base case: if there is one item in the array
    if index == len(arr)-1:
        return index
    
    #recursive call
    smallestIndex = masterClass.minIndex(arr, index + 1, l)

    #return smaller value from returned value from recursive call and current index
    if(arr[index] < arr[smallestIndex]):
      return index
    else:
      return smallestIndex

  #recursive function for selection sort
  def selectionSort (arr, len, cur):
    #base case 
    if cur == len:
      return -1

    #k = masterClass.minIndex(arr, cur, len-1)
    smallestIndex = arr.index(min(arr[cur:]))

     #check if index is the first index, if not, replace it with the first index
    if smallestIndex != cur:
      arr[smallestIndex], arr[cur] = arr[cur], arr[smallestIndex]

    #recursive call
    masterClass.selectionSort(arr, len, cur+1)

  #interative function for selection sort
  def selectionsort_(arr):
    #loop to iterate through all elements in list
    for i in range(len(arr)):
      #get index of smallest element in list
      smallestIndex = arr.index(min(arr[i:]))

      #check if index is the first index, if not, replace it with the first index
      if smallestIndex != i:
        arr[smallestIndex], arr[i] = arr[i], arr[smallestIndex]
      
    
  #takes two sorted arrays and merges them in a sorted manner
  def merge(first, second):
    flen, slen = 0, 0   #varaibles to iterate through both arrays
    sorted = []         #empty array to store combined array

    #while loop to iterate through array
    while flen < len(first) and slen < len(second):
        #add list elements to sorted array by comparing them one by one 
        if first[flen] < second[slen]:
            sorted.append(first[flen])
            flen += 1                   
        else:
            sorted.append(second[slen])
            slen += 1

    #add last element in array to sorted list
    sorted += first[flen:]
    sorted += second[slen:]
    return sorted   #return sorted array

  #merge sort function
  def mergeSort (arr):
    #base case: if there is lesser than two items in the list
    if len(arr) <= 1:
      return arr
    
    else:
      #get middle index of the list
      mid = len(arr)//2
      #recursive call, array sliced from start to middle
      first = masterClass.mergeSort(arr[:mid])

      #recursive call, array sliced from middle to end
      second = masterClass.mergeSort(arr[mid:])

      #merging two lists
      sorted = masterClass.merge(first, second)

    #return sorted array
    return sorted


    
