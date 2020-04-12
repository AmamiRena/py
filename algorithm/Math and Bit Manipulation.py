'''
1.
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Example
Given [1,2,2,1,3,4,3], return 4

Challenge
One-pass, constant extra space
'''
class Solution_Mathbit_1:
    def singleNum(self,array):
        array.sort()
        if array[0]!=array[1]:
            return array[0]
        if array[-1]!=array[-2]:
            return array[-1]
        length=len(array)
        c=0
        while c<length:
            if array[c]!=array[c+1]:
                return array[c]
            c+=2
    
    def singleNum_bits(self,array):
        mul=0
        for n in array:
            mul^=n
        return mul
mathbit_1=Solution_Mathbit_1()
print(mathbit_1.singleNum_bits([1,2,2,1,3,4,3]))
print(mathbit_1.singleNum_bits([1,2,2,5,5,3,4,4,3]))
print(mathbit_1.singleNum_bits([1,2,2,1,3,4,4]))
print(mathbit_1.singleNum_bits([1,2,2,1,3,3,4,5,5]))

'''
2.
Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.

Example
Given [1,1,2,3,3,3,2,2,4,1] return 4

Challenge
One-pass, constant extra space
'''
class Solution_Mathbit_2:
    def singleNum(self,array):
        array.sort()
        if array[0]!=array[1]:
            return array[0]
        if array[-1]!=array[-2]:
            return array[-1]
        length=len(array)
        c=0
        while c<length:
            if array[c]!=array[c+1]:
                return array[c]
            c+=3
    
    def singleNum_bits(self,array):
        list_1=map(self.tenToTwo,array)
        sum_=sum(list_1)
        list_2=[int(i) for i in str(sum_)]
        result=[str(i%3) for i in list_2]
        return self.twoToTen(int(''.join(result)))
    
    def tenToTwo(self,n):
        result=[]
        r=n
        while r>1:
            result.append(str(r%2))
            r=r//2
        result.append(str(r))
        return int(''.join(result[::-1]))
    
    def twoToTen(self,n):
        sum_=0
        n_str=str(n)[::-1]
        for i in range(len(n_str)):
            sum_+=int(n_str[i])*2**i
        return sum_
mathbit_2=Solution_Mathbit_2()
print(mathbit_2.singleNum_bits([1,1,2,3,3,3,2,2,4,1]))
print(mathbit_2.singleNum_bits([1,1,2,3,2,2,1,4,4,4]))
print(mathbit_2.singleNum_bits([2,2,2,4,4,4,6,6,6,9,9,9,12]))
print(mathbit_2.tenToTwo(16))
print(mathbit_2.twoToTen(11101))

'''
3.
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.
'''
class Solution_Mathbit_3:
    def singleNum_bits(self,array):
        mul=0
        for n in array:
            mul^=n
            low=mul&(-mul)
            res=[0,0]
        for n_ in array:
            if (n_&low)!=0:
                res[0]^=n_
            else:
                res[1]^=n_
        return res
mathbit_3=Solution_Mathbit_3()
print(mathbit_3.singleNum_bits([1,2,3,3,2,5]))
print(mathbit_3.singleNum_bits([1,2,3,3,2,4,4,5,5,6]))

'''
4.
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;

For n=5, return false;

Challenge
O(1) time
'''
class Solution_Mathbit_4:
    def checkPowerTwo(self,n):
        if n<1:
            return False
        else:
            return n&(n-1)==0

'''
5.
Determine the number of bits required to convert integer A to integer B

Example
Given n = 31, m = 14,return 2

(31)10=(11111)2

(14)10=(01110)2
'''
class Solution_Mathbit_5:
    def bitSwap(self,n_1,n_2):
        n_1=str(self.tenToTwo(n_1))
        n_2=str(self.tenToTwo(n_2))
        c=0
        d=0
        while c<min(len(n_1),len(n_2)):
            if n_1[c]!=n_2[c]:
                d+=1
            c+=1
        return d+abs(len(n_1)-len(n_2))
    
    def tenToTwo(self,n):
        result=[]
        r=n
        while r>1:
            result.append(str(r%2))
            r//=2
        result.append(str(r))
        return int(''.join(result[::-1]))
mathbit_5=Solution_Mathbit_5()
print(mathbit_5.bitSwap(31,14))
print(mathbit_5.tenToTwo(12))
print(mathbit_5.tenToTwo(19))
print(mathbit_5.bitSwap(12,19))

'''
6.
Write an algorithm which computes the number of trailing zeros in n factorial.

Example
11! = 39916800, so the out should be 2

Challenge
O(log N) time
'''
class Solution_Mathbit_6:
    def trailingZeros_1(self,n):
        if n<0:
            return -1
        c=0
        while n>0:
            n//=5
            c+=n
        return c
    
    def trailingZeros_2(self,n):
        if n==0:
            return 0
        if n<0:
            return -1
        return n//5+self.trailingZeros_2(n//5)
mathbit_6=Solution_Mathbit_6()
print(mathbit_6.trailingZeros_1(11))
print(mathbit_6.trailingZeros_2(11))

'''
7.
Given n, how many structurally unique BSTs (binary search trees)
that store values 1...n?

Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \ 6
  3      2     1       1   3      2
 /      /       \                  \ 6
2     1          2                  3
'''
