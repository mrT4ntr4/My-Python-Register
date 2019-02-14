# My Python Register
Noting down my flow with Python

[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

``` python
## Help about a module
help('modules') # This lists all built-in modules
module.__doc__ # To see some documentation about a specific module

## To Check BuiltIn Functions in a module
import hashlib # Need to import the module first
dir(hashlib)

## Importing Modules

####  greet.py
def msg():
 return 'Hey Wassup'

#### welcome.py
import greet
 greet.msg()

import greet as g # Can be aliased
 g.msg() 

### A module can be stand-alone runnable script.
# run_hello.py
if __name__ == '__main__':
 from greet import msg # specific functions can also be imported
 msg()

## 1. Testing Strings
str_hello='hello_World'
print(str_hello[0:5])

print type(str_hello) #### To check the dataType

print ''.join(reversed(str_hello)) #### To reverse a string easily

#### Ways to Concatenate string and int 

####1 (Using str() fn.)
x = 'list'
y = 12

print x+str(y)

####2 (Using % Op.)
print "%s%s"%(x,y)

####3 (Using format fn. Used by me here)
print "{}{}".format(x,y)



## 2. Sets & FrozenSets
set1 = {1,2,3,1,2,5,2,8,}
print set1

set2 = set('hello')
set2.add('y') ####Can add new elements easily
print set2

set3 = frozenset('lulzsec') ####Cannot add new elements
print "No. of Elements in FrozenSet_set3 ==> {}".format(len(set3))

## 3. Testing Complex Numbers data types
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

## 4. Lists
list = [11,22,11,'hello']
list.append('22') #### appending single element
print list

list.extend([55,'world'])  #### appending more than 2 elements
print list

list.insert(1, 'MyList') #### adding new element at a specific index
print list

print list[0:3] #### Outputs first 3 elements

list1=[1,2,3,4,5]
list2=[1,2,3]
list3=list1+list2
print list3 #### Concatenating 2 lists

list3.sort() #### Sorting Lists
print list3

print len(list3) #### Counts length of list

list3.remove(1) #### Removes 1st item whose value is equal to specified
print list3

list3.pop(6)  #### Removes element at index 6
print list3

print list3.count(3) #### Counts no. of times 3 appears

list3.reverse() #### Reverses a list using function
print list3

print list1[::-1]  #### Reverse a list by Slicing

for number in list3: #### Iterating through a list
	print number

```



