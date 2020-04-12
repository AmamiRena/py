'''
1.
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
'''

class Solution_Integer_1:
    def removeElement(self,array,value):
        if value not in array:
            return len(array),array
        else:
            result=list(filter(lambda x:x!=value,array))
        return len(result),result

integer_1=Solution_Integer_1()
print(integer_1.removeElement([0,4,4,0,0,2,4,4],4))
print(integer_1.removeElement([1,2,3,2,2,2,3,4],2))
print(integer_1.removeElement([0,4],3))

'''
2.
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Note
There is at least one subarray that it's sum equals to zero.
'''

class Solution_Integer_2:
    def subarray_0(self,array):
        sum_=0
        sum_list,result=[],[]
        for i in range(len(array)):
            sum_+=array[i]
            sum_list.append(sum_)
            if sum_==0:
                result.append([0,i])
            elif sum_ in sum_list[:-1]:
                index_2=self.findDuplicateNum(sum_list,sum_)[-2:]
                index_2[0]+=1
                result.append(index_2)
        return result
    
    def findDuplicateNum(self,array,n):
        result=[i for i in range(len(array)) if array[i]==n]
        return result

integer_2=Solution_Integer_2()
print(integer_2.subarray_0([-3,1,2,-3,4]))
print(integer_2.subarray_0([4,2,-3,1,6]))
print(integer_2.subarray_0([4,2,0,1,6]))
print(integer_2.findDuplicateNum([-3,1,2,-3,4],1))

'''
3.
Given an nonnegative integer array, find a subarray where the sum of numbers is k.
Your code should return the index of the first number and the index of the last number.

Example
Given [1, 4, 20, 3, 10, 5], sum k = 33, return [2, 4].
'''

class Solution_Integer_3:
    def subarraySum_k(self,array,k):
        sum_=0
        sum_list,result=[],[]
        for i in range(len(array)):
            sum_+=array[i]
            sum_list.append(sum_)
            if sum_==k:
                result.append([0,i])
            elif sum_-k in sum_list[:-1]:
                index_2=sum_list[:-1].index(sum_-k)
                index_2+=1
                result.append([index_2,len(sum_list)-1])
        return result
integer_3=Solution_Integer_3()
print(integer_3.subarraySum_k([1,4,20,3,10,5],33))
print(integer_3.subarraySum_k([1,4,28,3,30,5],33))
print(integer_3.subarraySum_k([33,4,20,3,10,5],33))

'''
4.
Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]

Challenge
O(nlogn) time
'''

class Solution_Integer_4:
    def subarraySum_close0(self,array):
        sum_=0
        sum_list,result=[],[]
        record=abs(array[0])
        for i in range(len(array)):
            sum_+=array[i]
            sum_list.append(sum_)
            temp=abs(sum_)
            if temp<=record:
                if temp<record:
                    record=temp
                    del result[-1]
                result.append([0,i])
            temp_list,step=self.stepinList(sum_list,record)
            if step<record:
                record=step
                result.clear()
            result+=temp_list
        return result
    
    def stepinList(self,array,step):
        result=[]
        if len(array)==1:
            return result,step
        temp_list=[abs(array[-1]-x) for x in array[:-1]]
        temp_step=min(temp_list)
        if temp_step<step:
            step=temp_step
        for i in range(len(temp_list)):
            if temp_list[i]<=step:
                result.append([i+1,len(array)-1])
        return result,step

integer_4=Solution_Integer_4()
print(integer_4.subarraySum_close0([-3,1,1,-3,5]))
print(integer_4.stepinList([-3],3))

'''
5.
Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.

Clarification
What is rotated array:

- For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
'''

class Solution_Integer_5:
    def recoverRotatedSortedArray(self,array):
        result=[]
        length=len(array)
        for i in range(length):
            element=min(array)
            result.append(element)
            array.remove(element)
        return result
integer_5=Solution_Integer_5()
print(integer_5.recoverRotatedSortedArray([2,3,4,1,5]))

'''
6.
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A=[1, 2, 3], return [6, 3, 2].
'''

class Solution_Integer_6:
    def productExcludeItself(self,array):
        result=[]
        if len(array)<=1:
            return result
        for i in range(len(array)):
            multiply_l,multiply_r=1,1
            left=array[:i]
            if len(left)>0:
                for n_1 in left:
                    multiply_l*=n_1
            right=array[i+1:]
            if len(right)>0:
                for n_2 in right:
                    multiply_r*=n_2
            multiply=multiply_l*multiply_r
            result.append(multiply)
        return result
integer_6=Solution_Integer_6()
print(integer_6.productExcludeItself([1,2,3]))
print(integer_6.productExcludeItself([1,2,3,4,5]))

'''
7.
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example

If nums = [3,2,2,1] and k=2, a valid answer is 1.

Note

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Challenge

Can you partition the array in-place and in O(n)?
'''
import numpy as np
class Solution_Integer_7:
    def partitionArray(self,array,k):
        result=np.partition(array,(0,len(array)-1))
        for i in range(len(result)):
            if result[i]>=k:
                return i
        return ''
integer_7=Solution_Integer_7()
print(integer_7.partitionArray([3,2,2,1],2))

'''
8.
Given an unsorted integer array, find the first missing positive integer.

Example
Given [1,2,0] return 3, and [3,4,-1,1] return 2.

Challenge
Your algorithm should run in O(n) time and uses constant space.
'''

class Solution_Integer_8:
    def firstMissingPositive(self,array):
        for i in range(len(array)):
            if i+1 not in array:
                return i+1
integer_8=Solution_Integer_8()
print(integer_8.firstMissingPositive([1,2,0]))
print(integer_8.firstMissingPositive([3,4,-1,1]))

'''
9.
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example

numbers=[2, 7, 11, 15], target=9

return [1, 2]

Note

You may assume that each input would have exactly one solution

Challenge

Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

class Solution_Integer_9:
    def twoSum(self,array,target):
        for n in array:
            if target-n in array:
                index_1=array.index(n)+1
                index_2=array.index(target-n)+1
                if index_1<index_2:
                    return [index_1,index_2]
                return [index_2,index_1]
        return 'No Solution'
integer_9=Solution_Integer_9()
print(integer_9.twoSum([2,7,11,15],9))

'''
10.
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1),(-1, -1, 2)

Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
'''

class Solution_Integer_10:
    def threeSum_0(self,array):
        result=[]
        if len(array)<3:
            return array
        result.sort()
        for i in range(len(array)):
            target=0-array[i]
            for j in array[i+1:]:
                if target-j in array[i+1:]:
                    temp=sorted([array[i],target-j,j])
                    if temp not in result:
                        result.append(temp)
        return result
integer_10=Solution_Integer_10()
print(integer_10.threeSum_0([-1,0,1,2,-1,-4]))

'''
11.
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution_Integer_11:
    def threeSumClosest(self,array,target):
        if len(array)<=3:
            return sum(array)
        array.sort()
        result=None
        for i in range(len(array)):
            left,right=i+1,len(array)-1
            while left<right:
                sum_=array[left]+array[right]+array[i]
                if result is None or abs(sum_-target)<abs(result-target):
                    result=sum_
                if sum_<=target:
                    left+=1
                else:
                    right-=1
        return result
integer_11=Solution_Integer_11()
print(integer_11.threeSumClosest([-1,2,1,-4],1))

'''
12.
Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''
import collections
class Solution_Integer_12:
    def removeDuplicates(self,array):
        return len(list(set(array)))
    def removeDuplicates_1(self,array):
        return len(collections.Counter(array).keys())
integer_12=Solution_Integer_12()
print(integer_12.removeDuplicates([1,1,2]))
print(integer_12.removeDuplicates_1([1,1,2]))

'''
13.
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''
import collections
class Solution_Integer_13:
    def removeDuplicates(self,array):
        length=0
        values=collections.Counter(array).values()
        for n in values:
            if n>2:
                length+=2
            else:
                length+=n
        return length
    
    def removeDuplicates_1(self,array):
        dict_0={}
        length=0
        for n in array:
            if n not in dict_0.keys():
                dict_0[n]=1
                length+=1
            else:
                if dict_0[n]==1:
                    dict_0[n]+=1
                    length+=1
        return length
integer_13=Solution_Integer_13()
print(integer_13.removeDuplicates([1,1,1,2,2,3]))
print(integer_13.removeDuplicates_1([1,1,1,2,2,3]))

'''
14.
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

Note
You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.
'''

class Solution_Integer_14:
    def mergeSortedArray(self,array_1,m,array_2,n):
        index=m+n-1
        while m>0 and n>0:
            if array_1[m-1]>array_2[n-1]:
                array_1[index]=array_1[m-1]
                m-=1
            else:
                array_1[index]=array_2[n-1]
                n-=1
            index-=1
        return array_1
integer_14=Solution_Integer_14()
print(integer_14.mergeSortedArray([1,2,3,'empty','empty'],3,[4,5],2))
print(integer_14.mergeSortedArray([1,2,'empty','empty','empty'],2,[3,4,5],3))
# print(integer_14.mergeSortedArray([3,4,5,'empty','empty'],3,[1,2],2))

'''
15.
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]
B=[2,4,5,6]
return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm
if one array is very large and the other is very small?
'''

class Solution_Integer_15:
    def mergeSortedArray(self,array_1,array_2):
        result=[]
        temp_array=array_1+array_2
        for i in range(len(temp_array)):
            each=min(temp_array)
            result.append(each)
            temp_array.remove(each)
        return result
    
    def mergeSortedArray_1(self,array_1,array_2):
        result=[]
        len_1,len_2=len(array_1),len(array_2)
        pointer_1,pointer_2=0,0
        while pointer_1<len_1 and pointer_2<len_2:
            if array_1[pointer_1]<=array_2[pointer_2]:
                result.append(array_1[pointer_1])
                pointer_1+=1
                if pointer_1==len_1 and pointer_2<len_2:
                    result+=array_2[pointer_2:]
            else:
                result.append(array_2[pointer_2])
                pointer_2+=1
                if pointer_2==len_2 and pointer_1<len_1:
                    result+=array_1[pointer_1:]
        return result
integer_15=Solution_Integer_15()
print(integer_15.mergeSortedArray([1,2,3,4],[2,4,5,6]))
print(integer_15.mergeSortedArray_1([1,2,3,4],[2,4,5,6]))

'''
16.
Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example
Given [4, 5, 1, 2, 3], return 3

Given [7, 9, 4, 5], return 5

Challenge
O(n) time.
'''
import math
class Solution_Integer_16:
    def findMedian(self,array):
        array.sort()
        length=len(array)-1
        if length%2==0:
            return array[math.ceil(length/2)]
        return array[int(length/2)]

integer_16=Solution_Integer_16()
print(integer_16.findMedian([4,5,1,2,3]))
print(integer_16.findMedian([7,9,4,5]))
print(integer_16.findMedian([7,9]))
print(integer_16.findMedian([5]))

'''
17.
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
'''

class Solution_Integer_17:
    def partitionArray(self,array):
        odd,even=[],[]
        for i in range(len(array)):
            temp=min(array)
            array.remove(temp)
            if temp%2!=0:
                odd.append(temp)
            else:
                even.append(temp)
        return odd+even
integer_17=Solution_Integer_17()
print(integer_17.partitionArray([1,2,3,4]))

'''
18.
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5,
2nd largest element is 4, 3rd largest element is 3 and etc.

Note
You can swap elements in the array

Challenge
O(n) time, O(1) extra memory.
'''

class Solution_Integer_18:
    def KthLargestElement(self,array,k):
        for i in range(k):
            temp=max(array)
            array.remove(temp)
        return temp
integer_18=Solution_Integer_18()
print(integer_18.KthLargestElement([9,3,2,4,8],3))

