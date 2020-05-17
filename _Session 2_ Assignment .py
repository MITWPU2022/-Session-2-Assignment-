#!/usr/bin/env python
# coding: utf-8

#                                             # Session 2: Assignment 1
# 

# # -------------------------------------------Task 1:-----------------------------------------------------------

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like
# Python's built-in function reduce()

# In[1]:


def doSum(x1, x2): 
    return x1 + x2

def myReduce(takeFunc, seq):
    first = seq[0]
    for i in seq[1:]:
        first = takeFunc(first, i)
    return first

print(myReduce(doSum, [1, 2, 3, 4,-1]))

print ("Sum on list [1,2,3] using custom reduce function "   + str(myReduce(doSum, [1,2,3])) )


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()
# 

# In[2]:


def myfilter(anyfunc, sequence):

 result = []
 for item in sequence:
  if anyfunc(item):
   result.append(item)
 return result

def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True

print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# 2.Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[3]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ( str(alphabet_list))

input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# 2.2. Implement a function longestWord() that takes a list of words and returns the longest one.
# 

# In[4]:



m=["amol","varsha","sachierfefdn","dwderefefderrfrefr","rreerewrfwrferwrefewrfde"]  


def longestWord(words_list):
   word_len = []
   
   for n in words_list:
       word_len.append((len(n), n))
   word_len.sort()
   
   return word_len[-1][1]


print(longestWord(m))


# In[5]:


def longestWord(m):
    p=[]
    for y in m:
        p.append((len(y),y))
    p.sort()

    return (p[-1][1])
             
longestWord(["amol","vsdsdsdsdsdsdsdarsha","sachierfefdn","dwderefefderrfrefr","dfd"] )


# # ----------------------------------Task 2:----------------------------------------------------------------

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.
# 

# In[16]:


import sys
import math
 
a = int(input('Please enter the first side of a triangle: '))
b = int(input('Please enter the second side of a triangle: '))
c = int(input('Please enter the third side of a triangle: '))
class triangle():
        def __init__(self,a,b,c):
                self.a = a
                self.b = b
                self.c = c
        def show(self):
            print("1st side of a triangle:",self.a)
            print("2nd side of a triangle:",self.b)
            print("3rd side of a triangle:",self.c)
    
class subclass(triangle):
    def __init__(self,*args):
        super(subclass, self).__init__(*args)             
        
    def area(self):
        s=(self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            #eturn self.area
        

sub = subclass(a,b,c)
sub.show()
print("Result ",sub.area())


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n.

# In[6]:


def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)


p= (filter_long_words(['this', 'words', 'are for testing'], 5))
for i in p:
    print (i)


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[7]:



wordlist = ["This", "is", "a", "beautiful", "day"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))


# In[8]:


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]


words = ['abv', 'try me', 'test']
print( map_to_lengths_for(words))
print (map_to_lengths_map(words))
print (map_to_lengths_lists(words))


# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise

# In[9]:


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


print (is_vowel(1))
print (is_vowel('a'))
print (is_vowel('b'))

