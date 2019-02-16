# My Python Register
Noting down my flow with Python

[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)
![banner-img](https://github.com/mrT4ntr4/My-Python-Register/blob/master/banner.webp)  



## Help about a module
```python
help('modules') # This lists all built-in modules
module.__doc__ # To see some documentation about a specific module
```
## To Check BuiltIn Functions in a module
```python
import hashlib # Need to import the module first
dir(hashlib)
```
## Importing Modules
```python
#  greet.py
def msg():
 return 'Hey Wassup'

# welcome.py
import greet
 greet.msg()

import greet as g # Can be aliased
 g.msg() 

# A module can be stand-alone runnable script.
if __name__ == '__main__':
 from greet import msg # specific functions can also be imported
 msg()
```
## Strings
```python
str_hello='hello_World'
print(str_hello[0:5])

print type(str_hello) # To check the dataType

print ''.join(reversed(str_hello)) # To reverse a string easily
```
### Ways to Concatenate string and int 
```console
Output : list12
```

#### I. Using str() fn.
```python
x = 'list'
y = 12

print x+str(y)
```
#### II. Using % Operator
```python
print "%s%s"%(x,y)
```
#### III. Using format function
```python
print "{}{}".format(x,y)
```

## Sets, FrozenSets and MultiSets
```python 
set1 = {1,2,3,1,2,5,2,8,}
print set1

set2 = set('hello')
set2.add('y') #Can add new elements easily
print set2

set3 = frozenset('lulzsec') #Cannot add new elements
print 'l' in set3 # Testing if element is present in a set, returns 'bool'
print 's' not in set3 # just opposite of 'in'
print "No. of Elements in FrozenSet_set3 ==> {}".format(len(set3))
```
```console
set([8, 1, 2, 3, 5])
set(['y', 'h', 'e', 'l', 'o'])
True
False
No. of Elements in FrozenSet_set3 ==> 6
```
```python

set4 = {10,20,30,40,50}
set5 = {30,40,50,60}

## Operations

### intersection (&)
print set4.intersection(set5)
print set4 & set5

### union (|)
print set4.union(set5)
print set4 | set5

### difference (-)
print set4.difference(set5)
print set4 - set5

### symmetric_difference (&)
print set4.symmetric_difference(set5)
print set4 ^ set5

### issubset (<=)
print set4.issubset(set5)
print set4 <= set5

### issuperset (>=)
print set4.issuperset(set5)
print set4 >= set5

### isdisjoint
print set4.isdisjoint(set5)
```

```console
set([40, 50, 30])
set([40, 10, 50, 20, 60, 30])
set([10, 20])
set([10, 20, 60])
False
False
False
```
```python
set6 = set4 | set5
set6.add(60)
set6.add(70)
print set6
print len(set6) # duplicates not allowed in sets
```
```console
set([70, 40, 10, 50, 20, 60, 30])
7
```

```python
# multisets.py

from collections import Counter
multisetCounter = Counter(['a','a','b'])
print multisetCounter

#OR Using multiset.py from pypi.org
import multiset
s1 = multiset.Multiset('aab')
print s1

```

```console
Counter({'a': 2, 'b': 1})
{a, a, b}
```

## Complex Numbers and other data types
```python
comp_num1 = 3 + 13j
print comp_num1
print(type(comp_num1))
comp_num2 = complex(2,5)
print comp_num2

print "Real Part (comp_num2) :: {}".format(comp_num2.real)
print "Imaginary Part (comp_num2) :: {}".format(comp_num2.imag)
print "Complex Conjugate (comp_num2) :: {}".format(comp_num2.conjugate())

float_num = 11122.2
print "Float :: {}".format(float_num)

long_num = 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111L
print "Long :: {}".format(long_num)
```

```console
(3+13j)
<type 'complex'>
(2+5j)
Real Part (comp_num2) :: 2.0
Imaginary Part (comp_num2) :: 5.0
Complex Conjugate (comp_num2) :: (2-5j)
Float :: 11122.2
Long :: 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
```

## Lists
```python
list = [11,22,11,'hello']
list.append('22') # appending single element
print list

list.extend([55,'world'])  # appending more than 2 elements
print list

list.insert(1, 'MyList') # adding new element at a specific index
print list

print list[0:3] # Outputs first 3 elements
```

```console
[11, 22, 11, 'hello', '22']
[11, 22, 11, 'hello', '22', 55, 'world']
[11, 'MyList', 22, 11, 'hello', '22', 55, 'world']
[11, 'MyList', 22]
```
```python
list1=[1,2,3,4,5]
list2=[1,2,3]
list3=list1+list2
print list3 # Concatenating 2 lists

print list2*3 # prints list2 3 times itself

list3.sort() # Sorting Lists
print list3

print len(list3) # Counts length of list

list3.remove(1) # Removes 1st item whose value is equal to specified
print list3
```
```console
[1, 2, 3, 4, 5, 1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 1, 2, 2, 3, 3, 4, 5]
8
[1, 2, 2, 3, 3, 4, 5]
```
```python
list3.pop(6)  # Removes element at index 6
print list3

print list3.count(3) # Counts no. of times 3 appears

list3.reverse() # Reverses a list using function
print list3

print list1[::-1]  # Reverse a list by Slicing
```
```console
[1, 2, 2, 3, 3, 4]
2
[4, 3, 3, 2, 2, 1]
[5, 4, 3, 2, 1]
```
```python
for number in list3: # Iterating through a list
	print number,  # note the , for printing in a single line

```
```console
4 3 3 2 2 1
```

## Dictionaries

```python
keyboard = {1:'CTRL', 2:'SHIFT', 4:'ENTER' }
print keyboard # lists contents of dictionary

print keyboard.values() # lists all values of all keys
print keyboard.keys() # gathers list all keys
```
```console
{1: 'CTRL', 2: 'SHIFT', 4: 'ENTER'}
['CTRL', 'SHIFT', 'ENTER']
[1, 2, 4]
```

### Accessing values

```console
Output : SHIFT
```
##### I. Using key
```python
print keyboard[2] 
```
##### II. Using get()
```python
print keyboard.get(2) 
```

### Deleting values
```console
[(1, 'CTRL'), (4, 'ENTER')]
```
##### I. Using del
```python
del keyboard[2] 
```
##### II. Using pop() 
```python
keyboard.pop(2) 
```
### Some Useful Built-In Functions
```python
print keyboard.items() # returns a *list of dict's (key,value) tuple pairs

dup = keyboard.copy() # duplicates a predefined dict
print dup

print keyboard.has_key(2) # Checks for a key in dict, Return bool
```
```console
[(1, 'CTRL'), (4, 'ENTER')]
{1: 'CTRL', 4: 'ENTER'}
False
```

```python
keys = {1,2,3}
value = 'NUMPAD'

kb2 = dict.fromkeys(keys, value) # Using fromkeys to create a dict from a sequence
print(kb2)

print len(kb2) # Counts the no. of (key,value) pair

print cmp(dup,kb2)
# returns 0 if both dictionaries are equal, -1 if kb2 < dup and 1 if kb2 > dup.
```
```console
{1: 'NUMPAD', 2: 'NUMPAD', 3: 'NUMPAD'}
3
-1
```

```python
keyboard.popitem() # pops out the first (key,value) pair
print keyboard

keyboard.clear() # Deletes every (key,value) pair present in the dictoinary
print keyboard
```
```console
{4: 'ENTER'}
{}
```

## Tuples

```python
tuple1 = 1,2,3,4,5
tuple1 = (1,2,3,4,5)

print tuple1
print tuple1[4]

tuple2 = () # Declaring an Empty Tuple
print tuple2

tuple3 = 1,
print tuple3
print type(tuple3) # Checking data Type
```
```console
(1, 2, 3, 4, 5)
5
()
(1,)
<type 'tuple'>
```
```python
tuple4 = tuple('hello')
print tuple4

list1 = ['r','o','y']
tuple5 = tuple(list1) # Creating tuple from list
print tuple5
```
```console
('h', 'e', 'l', 'l', 'o')
('r', 'o', 'y')
```
```python
tuple6 = ('github') #Tuple with Loop
for i in range(3):
	tuple6 = tuple6,
	print tuple6
```
```console
('github',)
(('github',),)
((('github',),),)
```
```python
tuple7 = tuple4,tuple5 # Nesting Tuples
print tuple7

tuple8 = ('hi',) * 2
print tuple8

tuple8 += ('github',) # Concatenation
print tuple8
```
```console
(('h', 'e', 'l', 'l', 'o'), ('r', 'o', 'y'))
('hi', 'hi')
('hi', 'hi', 'github')
```
```python
numbers = (1,2,3)
a,b,c = numbers
print a

x, = 1,  # x is the value 1
print type(x)
x = 1,   # x is the tuple (1,)
print type(x)
```
```console
1
<type 'int'>
<type 'tuple'>
```
```python
# Slicing of a Tuple 
tuple9 = (10,20,30) 
print(tuple9[2:]) # Only Display 3rd Element
print(tuple9[::-1]) # Reversing the Tuple  
print(tuple9[1:3]) # Printing elements in a Range 

revTuple = tuple(reversed(('hello'))) #Reversing using reversed()
print revTuple
```
```console
(30,)
(30, 20, 10)
(20, 30)
('o', 'l', 'l', 'e', 'h')
```
```python
t1 = (11,22,33,44)
t2 = (19,22,44,45)
t3 = (11,22,33,44)
t4 = ('a','b','c','d','e')

print cmp(t1,t2) # Returns '-1' as t2's elements are greater than t1's
print cmp(t1,t3) # Returns '0' as both tuples have exactly same elements 
print cmp(t4,t1) # Returns '1' as numbers is considered smaller than chars
```
```console
-1
0
1
```
```python
t1 = (1, 0, 2, 5, 4, 2, 4)
t2 = ('a','b','bee','bug')
print len(t1) # Counts no. of elements
print t1.count(2) # Counts the no. of times an element appears in tuple
```
```console
7
2
```
```python
print max(t1) # Numbers sorting
print max(t2) # Sorting Alphabetically

print min(t1) 
print min(t2)
```
```console
5
bug
0
a
```
```python
# sum()	Sums up the numbers in the tuple
print sum(t1)

print sorted((66,234,20)) # Returns sorted list
```
```console
18
[0, 1, 2, 2, 4, 4, 5]
```
```python
# all() Returns true if all element are true or if tuple is empty

l = [1, 3, 4, 5]  # all values true
print all(l)

l = [0, False] # all values false
print all(l)

l = [1, 3, 4, 0] # one false value
print all(l)

l = [0, False, 5]  # one true value
print all(l)

l = [] # empty iterable
print all(l)
```
```console
True
False
False
False
True
```
```python
# any() Returns true if any element of the tuple is true, also false if tuple empty 
l = [1, 3, 4, 0]
print(any(l)) 

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))
```
```console
True
False
True
False
```
```python
#map() applies a given function to each item of an iterable and returns a list with result.
def Square(n):
  return n*n

numbers = (1, 2, 3, 4)
sqList = map(Square, numbers)
print sqList
```
```console
[1, 4, 9, 16]
```
```python
t1 = (1,2,3)
del t1 
print t1
```
```console
print t1
NameError: name 't1' is not defined
```

# Random File Operations

```python
import base64

# Using a list to read line by line 
with open('random.txt','r+') as fl: # Read & Write both with 'r+'
	contentList = fl.readlines()
	beLine = base64.b64encode(str(contentList[3])) # base64 encodes the 4th item in list
	if (contentList[-1] != beLine):	# Check if last line not encoded
	 fl.write("\n"+beLine) # If not encoded then encode it and write to the file

# Another method -- Simply Read as Strings (for Small Files)
with open('random.txt', 'r') as fl:   
	content = fl.read()  

#Decoding the last line which was encoded by us
print content + " when decoded gives :: " + base64.b64decode(str(contentList[-1]))
```
```
hi
hello
hola
hey
aGV5Cg== when decoded gives :: hey
```






