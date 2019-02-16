# Tuples

tuple1 = 1,2,3,4,5
tuple1 = (1,2,3,4,5)

print tuple1
print tuple1[4]

tuple2 = () # Declaring an Empty Tuple
print tuple2

tuple3 = 1,
print tuple3
print type(tuple3) # Checking data Type

tuple4 = tuple('hello')
print tuple4

list1 = ['r','o','y']
tuple5 = tuple(list1) # Creating tuple from list
print tuple5

tuple6 = ('github') #Tuple with Loop
for i in range(3):
	tuple6 = tuple6,
	print tuple6

tuple7 = tuple4,tuple5 # Nesting Tuples
print tuple7

tuple8 = ('hi',) * 2
print tuple8

tuple8 += ('github',) # Concatenation
print tuple8

numbers = (1,2,3)
a,b,c = numbers
print a

a, = 1,  # a is the value 1
print type(a)
a = 1,   # a is the tuple (1,)
print type(a)

# Slicing of a Tuple 
tuple9 = (10,20,30) 
print(tuple9[2:]) # Only display 3rd Element
print(tuple9[::-1]) # Reversing the Tuple  
print(tuple9[1:3]) # Printing elements in a Range 


revTuple = tuple(reversed(('hello'))) #Reversing using reversed()
print revTuple

t1 = (11,22,33,44)
t2 = (19,22,44,45)
t3 = (11,22,33,44)
t4 = ('a','b','c','d','e')

print cmp(t1,t2) # Returns '-1' as t2's elements are greater than t1's
print cmp(t1,t3) # Returns '0' as both tuples have exactly same elements 
print cmp(t4,t1) # Returns '1' as numbers is considered smaller than chars

t1 = (1, 0, 2, 5, 4, 2, 4) 
t2 = ('a','b','bee','bug')
print len(t1) # Counts no. of elements
print t1.count(2) # Counts the no. of times an element appears in tuple

print max(t1) # Numbers sorting
print max(t2) # Sorting Alphabetically

print min(t1) 
print min(t2)

# sum()	Sums up the numbers in the tuple
print sum(t1)

print sorted(t1) # Returns Sorted list

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

# any() Returns true if any element of the tuple is true, also false if tuple empty 
l = [1, 3, 4, 0]
print(any(l)) 

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

#map() applies a given function to each item of an iterable and returns a list with result.
def Square(n):
  return n*n

numbers = (1, 2, 3, 4)
sqList = map(Square, numbers)
print sqList

'''
del t1 
print t1
'''