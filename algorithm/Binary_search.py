'''
1.
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than $$2^{32}$$, can your code work properly?
'''

class Solution_Binary_1:
    def binarySearch(self,array,target):
        lowerbound=0
        upperbound=len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                if pointer==0:
                    return 0
                while array[pointer]==target:
                    pointer-=1
                return pointer+1
            elif target<array[pointer]:
                upperbound=pointer
                if lowerbound==upperbound:
                    return -1
            elif target>array[pointer]:
                lowerbound=pointer+1
        return -1
binary_1=Solution_Binary_1()
print(binary_1.binarySearch([1,2,3,3,4,5,10],3))
print(binary_1.binarySearch([1,1,2,3,4,5],2))
print(binary_1.binarySearch([1,2,3,4,5],3))
print(binary_1.binarySearch([1,2,3,4,5],4))
print(binary_1.binarySearch([1,2,3,4,5],1))
print(binary_1.binarySearch([1,2,3,4,5],5))
print(binary_1.binarySearch([1,2,3,4,5],0))
print(binary_1.binarySearch([1,2,3,4,5],6))
print(binary_1.binarySearch([1,3,5,7,9],4))

'''
2.
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Challenge
O(log(n)) time
'''

class Solution_Binary_2:
    def searchInsert(self,array,target):
        lowerbound=0
        upperbound=len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                return pointer
            elif target<array[pointer]:
                upperbound=pointer
                if upperbound==lowerbound:
                    return lowerbound
            elif target>array[pointer]:
                lowerbound=pointer+1
        return lowerbound
binary_2=Solution_Binary_2()
print(binary_2.searchInsert([1,3,5,6],5))
print(binary_2.searchInsert([1,3,5,6],1))
print(binary_2.searchInsert([1,3,5,6],6))
print(binary_2.searchInsert([1,3,5,6],2))
print(binary_2.searchInsert([1,3,5,6],7))
print(binary_2.searchInsert([1,3,5,6],0))
print(binary_2.searchInsert([1,3,5,6],4))

'''
3.
Given a sorted array of n integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

Challenge
O(log n) time.
'''

class Solution_Binary_3:
    def searchRange(self,array,target):
        lowerbound,upperbound=0,len(array)-1
        result=[-1,-1]
        switch_0=False
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                if pointer==0:
                    switch_0=True
                    result[0]=0
                if not switch_0:
                    record=pointer
                    while array[pointer]==target:
                        pointer-=1
                    result[0]=pointer+1
                    pointer=record
                while pointer<len(array) and array[pointer]==target:
                    pointer+=1
                result[1]=pointer-1
                return result
            elif target<array[pointer]:
                upperbound=pointer
                if upperbound==lowerbound:
                    return result
            elif target>array[pointer]:
                lowerbound=pointer+1
        return result
    
    def searchRange_1(self,array,target):
        result=[-1,-1]
        lowerbound,upperbound=0,len(array)-1
        while lowerbound+1<upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                upperbound=pointer
            elif target<array[pointer]:
                upperbound=pointer
            elif target>array[pointer]:
                lowerbound=pointer
        if array[lowerbound]==target:
            result[0]=lowerbound
        elif array[upperbound]==target:
            result[0]=upperbound

        lowerbound,upperbound=0,len(array)-1
        while lowerbound+1<upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                lowerbound=pointer
            elif target<array[pointer]:
                upperbound=pointer
            elif target>array[pointer]:
                lowerbound=pointer
        if array[upperbound]==target:
            result[1]=upperbound
        elif array[lowerbound]==target:
            result[1]=lowerbound
        return result

binary_3=Solution_Binary_3()
print(binary_3.searchRange_1([5,7,7,8,8,10],5))
print(binary_3.searchRange_1([5,7,7,8,8,10],7))
print(binary_3.searchRange_1([5,7,7,8,8,10],8))
print(binary_3.searchRange_1([5,7,7,8,8,10],10))
print(binary_3.searchRange_1([5,7,7,8,8,10],6))

'''
4.
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Example
Given n = 5:
isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
Here we are 100% sure that the 4th version is the first bad version.

Note
Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is VersionControl.isBadVersion(v)

Challenge
You should call isBadVersion as few as possible.
'''

class Solution_Binary_4:
    def isBadVersion(self,num):
        return num>0
    
    def findFirstBadVersion(self,num):
        lowerbound,upperbound=0,num+1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if self.isBadVersion(pointer):
                upperbound=pointer
            else:
                lowerbound=pointer+1
        return lowerbound

'''
5.
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
'''

class Solution_Binary_5:
    # 1-D
    def searchMatrix_1(self,matrix,target):
        row,column=len(matrix),len(matrix[0])
        lowerbound,upperbound=0,row*column-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            index_1=pointer//column
            if matrix[index_1][pointer-index_1*column]==target:
                return True
            elif target<matrix[index_1][pointer-index_1*column]:
                upperbound=pointer
                if upperbound==lowerbound:
                    return False
            elif target>matrix[index_1][pointer-index_1*column]:
                lowerbound=pointer+1
        return False
    
    # 2-D
    def searchMatrix_2(self,matrix,target):
        lowerbound,upperbound=0,len(matrix)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if matrix[pointer][-1]==target:
                return True
            elif target<matrix[pointer][-1]:
                upperbound=pointer
                if upperbound==lowerbound:
                    temp_row=matrix[pointer]
                    break
            elif target>matrix[pointer][-1]:
                lowerbound=pointer+1
        temp_row=matrix[pointer]

        lowerbound,upperbound=0,len(matrix[0])-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if temp_row[pointer]==target:
                return True
            elif target<temp_row[pointer]:
                upperbound=pointer
                if upperbound==lowerbound:
                    return False
            elif target>temp_row[pointer]:
                lowerbound=pointer+1
        return False

binary_5=Solution_Binary_5()
print(binary_5.searchMatrix_1([[1,3,5,7],[10,11,16,20],[23,30,34,50]],1))
print(binary_5.searchMatrix_1([[1,3,5,7],[10,11,16,20],[23,30,34,50]],50))
print(binary_5.searchMatrix_1([[1,3,5,7],[10,11,16,20],[23,30,34,50]],11))
print(binary_5.searchMatrix_1([[1,3,5,7],[10,11,16,20],[23,30,34,50]],9))
print(binary_5.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,50]],1))
print(binary_5.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,50]],50))
print(binary_5.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,50]],11))
print(binary_5.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,50]],7))
print(binary_5.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,50]],9))

'''
6.
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
'''

class Solution_Binary_6:
    def findPeak(self,array):
        lowerbound,upperbound=0,len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]<array[pointer+1]:
                lowerbound=pointer
            elif array[pointer]<array[pointer-1]:
                upperbound=pointer+1
            else:
                return pointer
binary_6=Solution_Binary_6()
print(binary_6.findPeak([1,2,3,1]))
print(binary_6.findPeak([1,2,3,4,5,6,4,2]))
print(binary_6.findPeak([1,2,5,4,3,2]))

'''
7.
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.
For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time
'''

class Solution_Binary_7:
    def searchNum(self,array,target):
        lowerbound,upperbound=0,len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                return pointer
            elif array[pointer]>array[lowerbound]:
                if target==array[lowerbound]:
                    return lowerbound
                if target>array[lowerbound] and target<array[pointer]:
                    upperbound=pointer
                else:
                    lowerbound=pointer+1
            elif array[pointer]<array[lowerbound]:
                if target==array[lowerbound]:
                    return lowerbound
                if target<array[lowerbound] and target>array[pointer]:
                    lowerbound=pointer+1
                else:
                    upperbound=pointer
            else:
                if array[pointer]==array[upperbound]:
                    return -1
binary_7=Solution_Binary_7()
print(binary_7.searchNum([4,5,1,2,3],2))
print(binary_7.searchNum([5,6,7,8,1,2,3,4],6))
print(binary_7.searchNum([5,6,7,8,1,2,3,4],1))
print(binary_7.searchNum([5,6,1,2,3,4],4))
print(binary_7.searchNum([4,5,1,2,3],0))
print(binary_7.searchNum([4,5,1,2,3],6))

'''
8.
Follow up for "Search in Rotated Sorted Array": What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
'''

class Solution_Binary_8:
    def searchNum(self,array,target):
        lowerbound,upperbound=0,len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]==target:
                return True
            elif array[pointer]>array[lowerbound]:
                if target==array[lowerbound]:
                    return True
                if target>array[lowerbound] and target<array[pointer]:
                    upperbound=pointer
                else:
                    lowerbound=pointer+1
            elif array[pointer]<array[lowerbound]:
                if target==array[lowerbound]:
                    return True
                if target<array[lowerbound] and target>array[pointer]:
                    lowerbound=pointer+1
                else:
                    upperbound=pointer
            else:
                if array[pointer]==array[upperbound]:
                    return False
                else:
                    lowerbound+=1
binary_8=Solution_Binary_8()
print(binary_8.searchNum([3,4,4,5,7,0,1,2],4))
print(binary_8.searchNum([2,5,6,0,0,1,2],6))
print(binary_8.searchNum([2,5,6,0,0,1,2],3))
print(binary_8.searchNum([4,4,4,5,2],5))

'''
9.
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0

Note
You may assume no duplicate exists in the array.
'''

class Solution_Binary_9:
    def findMin(self,array):
        lowerbound,upperbound=0,len(array)-1
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            if array[pointer]<array[pointer+1] and array[pointer]<array[pointer-1]:
                return array[pointer]
            if array[pointer]>array[lowerbound]:
                if array[pointer]>array[upperbound]:
                    lowerbound=pointer+1
                else:
                    upperbound=pointer
            elif array[pointer]<array[lowerbound]:
                upperbound=pointer
            elif pointer==0:
                return array[0]
binary_9=Solution_Binary_9()
print(binary_9.findMin([4,5,6,7,0,1,2]))
print(binary_9.findMin([1,2,3,4,5,6,7]))
print(binary_9.findMin([3,4,1,2]))

'''
10.
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.

Challenge
The overall run time complexity should be O(log (m+n)).
'''

class Solution_Binary_10:
    def findMedianSortedArray(self,array_1,array_2):
        combine=array_1+array_2
        combine.sort()
        length=len(combine)
        if length%2==0:
            return (combine[length//2]+combine[length//2-1])/2
        else:
            return combine[length//2]
binary_10=Solution_Binary_10()
print(binary_10.findMedianSortedArray([1,2,3,4,5,6],[2,3,4,5]))
print(binary_10.findMedianSortedArray([1,2,3],[4,5]))

'''
11.
Square root
'''
class Solution_Binary_11:
    def sqrt(self,n):
        error=1e-14
        lowerbound,upperbound=0,n
        pointer=(lowerbound+upperbound)/2
        while abs(pointer**2-n)>error:
            pointer=(lowerbound+upperbound)/2
            if pointer**2>n:
                upperbound=pointer
            elif pointer**2<n:
                lowerbound=pointer
        return pointer
binary_11=Solution_Binary_11()
print(binary_11.sqrt(13))
print(binary_11.sqrt(25))

'''
12.
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Example
For L=[232, 124, 456], k=7, return 114.

Note
You couldn't cut wood into float length.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''

class Solution_Binary_12:
    def woodCut(self,array,k):
        lowerbound,upperbound=0,max(array)
        while lowerbound<=upperbound:
            pointer=(lowerbound+upperbound)//2
            n=sum(x//pointer for x in array)
            if n<k:
                upperbound=pointer
            elif n<k:
                lowerbound=pointer
            else:
                return pointer
binary_12=Solution_Binary_12()
print(binary_12.woodCut([232,124,456],7))