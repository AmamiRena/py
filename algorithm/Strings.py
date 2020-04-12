'''
1. Return the index of a string, or either -1.
KMP Algorithms
'''

class Solution_String_1:
    def find_str_simple(self,source,target):
        try:
            return source.index(target)
        except:
            return -1
    
    def find_str_complicated(self,source,target):
        if source is None or target is None:
            return -1
        for i in range(len(source)-len(target)+1):
            for j in range(len(target)):
                if source[i+j]!=source[j]:
                    break
            else:
                return i
        return -1


'''
2. check if a string is anagrams
'''

import collections

class Solution_String_2:

    def check_str_simple(self,str_1,str_2):
        return sorted(str_1)==sorted(str_2)

    def check_str_2(self,str_1,str_2):
        return collections.Counter(str_1)==collections.Counter(str_2)

'''
3. check if string A is contained in string B

For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.
'''

import collections

class Solution_String_3:

    def Compare_str(self,str_1,str_2):
        string_count=collections.defaultdict(int)
        for s_1 in str_1:
            string_count[s_1]+=1
        for s_2 in str_2:
            if s_2 not in string_count:
                return False
            elif string_count[s_2]<=0:
                return False
            else:
                string_count[s_2]-=1
        return True

# string_3=Solution_String_3()
# print(string_3.Compare_str('ABCD','AABC'))

'''
4.

Given an array of strings, return all groups of strings that are anagrams.

Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

All inputs will be in lower-case
'''

class Solution_String_4:
    def anagrams_1(self,strs):
        
        if len(strs)<2:
            return strs
        result=[]
        visited=[False]*len(strs)
        for i_1,s_1 in enumerate(strs):
            hasAnagrams=False
            for i_2,s_2 in enumerate(strs):
                if i_2>i_1 and not visited[i_2] and self.isAnagrams(s_1,s_2):
                    result.append(s_2)
                    visited[i_2]=True
                    hasAnagrams=True
            if not visited[i_1] and hasAnagrams:
                        result.append(s_1)
        return result
    def isAnagrams(self,str_1,str_2):
        if sorted(str_1)==sorted(str_2):
            return True
        return False
    
    def anagrams_2(self,strs):
        strDict={}
        result=[]
        for s_ in strs:
            if ''.join(sorted(s_)) not in strDict.keys():
                strDict[''.join(sorted(s_))]=1
            else:
                strDict[''.join(sorted(s_))]+=1
        for s_ in strs:
            if strDict[''.join(sorted(s_))]>1:
                result.append(s_)
        return result


string_4_1=Solution_String_4()
print(string_4_1.anagrams_1(['ab','ba','cd','dc','e']))
print(string_4_1.anagrams_1(['lint','intl','inlt','code']))

string_4_2=Solution_String_4()
print(string_4_2.anagrams_2(['ab','ba','cd','dc','e']))
print(string_4_2.anagrams_2(['lint','intl','inlt','code']))

'''
5.

Given 2 strings, find the longest common substring.
Return the length of it.

Example
Given A='ABCD', B='CBCE', return 2

Note
must occur continuously in original string
'''

class Solution_String_5:
    def longestCommonString(self,str_1,str_2):
        result,record=0,0
        for i_1,s_1 in enumerate(str_1):
            result=0
            for i_2,s_2 in enumerate(str_2):
                result=0
                if s_1==s_2:
                    for set_1 in zip(str_1[i_1:],str_2[i_2:]):
                        if set_1[0]==set_1[1]:
                            result+=1
                            if result>record:
                                record=result
                        else:
                            break
        return record
    
    def longestCommonString_1(self,str_1,str_2):
        result,record=0,0
        len_1,len_2=len(str_1),len(str_2)
        temp_list=[[0 for j in range(len_2)] for i in range(len_1)]
        for i in range(len_1):
            for j in range(len_2):
                result=0
                if str_1[i]==str_2[j]:
                    temp_list[i][j]+=1
                    result+=1
                    if i>0 and j>0 and str_1[i-1]==str_2[j-1]:
                        result+=1
                    if record<result:
                        record=result
        return record
string_5=Solution_String_5()
print(string_5.longestCommonString_1('ABCD','CBCE'))
print(string_5.longestCommonString_1('ABCD','ACFE'))

'''
6.

Given a string and an offset, rotate string by offset.
(rotate from left to right)

Example
Given 'abcdefg'
offset=1 => 'abcdefg'
offset=2 => 'gabcdef'
offset=3 => 'fgabcde'
offset=4 => 'efgabcd'
'''

class Solution_String_6:
    def rotateString_1(self,str_,offset):
        if str_ is None or len(str_)==0:
            return str_
        offset%=len(str_)
        offset-=1
        str_b4=str_[len(str_)-offset:]
        print(str_b4)
        str_after=str_[:len(str_)-offset]
        print(str_after)
        result=str_b4+str_after
        return result
    
    def rotateString_2(self,str_,offset):
        if str_ is None or len(str_)==0:
            return str_
        offset%=len(str_)
        self.reverse(str_,0,len(str_)-offset-1)
        self.reverse(str_,len(str_)-offset,len(str_)-1)
        self.reverse(str_,0,len(str_)-1)
    def reverse(self,str_,start,end):
        while start<end:
            str_[start],str_[end]=str_[end],str_[start]
            start+=1
            end-=1

string_6=Solution_String_6()
print(string_6.rotateString_1('',4))
print(string_6.rotateString_2('abcdefg',2))

'''
7.
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Example
Clarification

- What constitutes a word?
A sequence of non-space characters constitutes a word.

- Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.

- How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

class Solution_String_7:
    def reverseWords(self,str_):
        list_=str_.strip().split(' ')
        for i in list_:
            if i=='':
                list_.remove(i)
        result=' '.join(reversed(list_))
        return result

string_7=Solution_String_7()
print(string_7.reverseWords('the sky is blue'))

'''
8.
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
Note
Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.

Challenge
O(n) time without extra memory.
'''

class Solution_String_8:
    def isPalindrome(self,strs):
        if not strs:
            return True
        l,r=0,len(strs)-1
        while l<r:
            if not strs[l].isalnum():
                l+=1
                continue
            if not strs[r].isalnum():
                r-=1
                continue
            if strs[l].lower()==strs[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

string_8=Solution_String_8()
print(string_8.isPalindrome('A man, a plan, a canal: Panama'))
print(string_8.isPalindrome('race a car'))

'''
9.
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
'''

class Solution_String_9:
    def longestPalindrome(self,strs):
        if not strs:
            return ''
        longest,left,right=0,0,0
        for i in range(0,len(strs)):
            for j in range(i+1,len(strs)+1):
                substrs=strs[i:j]
                if self.isPalindrome(substrs) and len(substrs)>longest:
                    longest=len(substrs)
                    left,right=i,j
        result=strs[left:right]
        return result

    def isPalindrome(self,strs):
        if not strs:
            return True
        l,r=0,len(strs)-1
        while l<r:
            if not strs[l].isalnum():
                l+=1
                continue
            if not strs[r].isalnum():
                r-=1
                continue
            if strs[l].lower()==strs[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

string_9=Solution_String_9()
print(string_9.longestPalindrome('abcdzdcab'))

'''
10.
Write a method to replace all spaces in a string with %20. 
The string is given in a characters array, you can assume it has enough space 
for replacement and you are given the true length of the string.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python，please use characters array instead of string.

Challenge
Do it in-place.
'''

class Solution_String_10:
    def replaceSpace(self,strs):
        result=strs.replace(' ','%20')
        return result

string_10=Solution_String_10()
print(string_10.replaceSpace("Mr John Smith"))

'''
11.
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("cb","?a") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
isMatch("adceb", "*a*b") → true
isMatch("acdcb", "a*c?b") → false
'''
class Solution_String_11:
    def isMatch(self,str_1,str_2):
        pointer_1,pointer_2=0,0
        asterisk=False
        while pointer_1<len(str_1):
            if pointer_2<len(str_2) and (str_1[pointer_1]==str_2[pointer_2] or str_2[pointer_2]=='?'):
                pointer_1+=1
                pointer_2+=1
                asterisk=False
                continue
            if pointer_2<len(str_2) and str_2[pointer_2]=='*':
                pointer_2+=1
                asterisk=True
                if pointer_2<len(str_2) and str_2[pointer_2]=='?':
                    pointer_2+=1
                    try:
                        index=str_1.find(str_2[pointer_2])
                    except:
                        return False
                    pointer_1=index
                continue
            if asterisk:
                if str_1[pointer_1]==str_1[-1] and str_2[-1]!='*':
                    return False
                pointer_1+=1
                continue
            return False
        return True

string_11=Solution_String_11()
print(string_11.isMatch('aa','*'))
print(string_11.isMatch('aa','a*'))
print(string_11.isMatch('ab','?*'))
print(string_11.isMatch('aab','c*a*b'))
print(string_11.isMatch('adceb','*a*b'))
print(string_11.isMatch('adceb','a*c*f'))
print(string_11.isMatch('acdcb','a*c?b'))
print(string_11.isMatch('aaabbb','a*b*'))
print(string_11.isMatch('aaaabaaaab','a*b*b'))
print(string_11.isMatch('abcdefg','a*?g'))

'''
12.
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Have you met this question in a real interview? Yes
Example
Given s = "Hello World", return 5.

Note
A word is defined as a character sequence consists of non-space characters only.
copy
'''
class Solution_String_12:
    def lenOfLastWord(self,strs):
        strs_list=strs.split(' ')
        return len(strs_list[-1])

string_12=Solution_String_12()
print(string_12.lenOfLastWord('Hello World'))

'''
13.
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Example
Given n = 5, return "111221".

Note
The sequence of integers will be represented as a string.
'''
import collections
class Solution_String_13:
    def countAndSay_1(self,n):
        if n<2:
            return '1'
        c=2
        num='11'
        switch=False
        while c<n:
            temp_store,result='',''
            for i_ in range(1,len(num)):
                if num[i_]!=num[i_-1]:
                    result+=num[i_-1]
                    temp_store+=self.countKey(result)
                    result=''
                    switch=True
                    if i_==len(num)-1:
                        result+=num[i_]
                        switch=False
                else:
                    switch=False
                    result+=num[i_-1]
                    if i_==len(num)-1:
                        result+=num[i_]
            if not switch:
                temp_store+=self.countKey(result)
            num=temp_store
            c+=1
        return num
    
    def countKey(self,strs):
        store=''
        dic=collections.Counter(strs)
        count=[i for i in dic.values()][0]
        key=[i for i in dic.keys()][0]
        store+=str(count)
        store+=str(key)
        return store
    
    def consecutiveStr(self,strs):
        if len(strs)==1:
            return [strs]
        list_store=[]
        temp=''
        for i in range(1,len(strs)):
            if strs[i]==strs[i-1]:
                temp+=strs[i-1]
            else:
                temp+=strs[i-1]
                list_store.append(temp)
                temp=''
        temp+=strs[i]
        list_store.append(temp)
        return list_store
    
    def countAndSay_2(self,n):
        num='1'
        c=1
        while c<n:
            strings=''
            list_num=self.consecutiveStr(num)
            for i in list_num:
                strings+=self.countKey(i)
            num=strings
            c+=1
        return num

string_13=Solution_String_13()
print(string_13.countAndSay_1(2))
print(string_13.countAndSay_1(3))
print(string_13.countAndSay_1(4))
print(string_13.countAndSay_1(5))
print(string_13.countAndSay_1(6))
print(string_13.countAndSay_1(7))
print(string_13.countAndSay_2(2))
print(string_13.countAndSay_2(3))
print(string_13.countAndSay_2(4))
print(string_13.countAndSay_2(5))
print(string_13.countAndSay_2(6))
print(string_13.countAndSay_2(7))