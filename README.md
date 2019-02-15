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

## Sets & FrozenSets
```python
set1 = {1,2,3,1,2,5,2,8,}
print set1

set2 = set('hello')
set2.add('y') #Can add new elements easily
print set2

set3 = frozenset('lulzsec') #Cannot add new elements
print 'l' in set3 # Testing if element is present in a set, returns bool
print "No. of Elements in FrozenSet_set3 = {}".format(len(set3))
```

```console
set([8, 1, 2, 3, 5])
set(['y', 'h', 'e', 'l', 'o'])
True
No. of Elements in FrozenSet_set3 = 6
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
