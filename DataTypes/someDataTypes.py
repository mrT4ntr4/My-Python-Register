
##  Testing Strings
str_hello='hello_World'
print(str_hello[0:5])

print type(str_hello) # To check the dataType

print ''.join(reversed(str_hello)) # To reverse a string easily

# Ways to Concatenate string and int 

#1 (Using str() fn.)
x = 'list'
y = 12

print x+str(y)

#2 (Using % Op.)
print "%s%s"%(x,y)

#3 (Using format fn. Used by me here)
print "{}{}".format(x,y)



##  Sets & FrozenSets
set1 = {1,2,3,1,2,5,2,8,}
print set1

set2 = set('hello')
set2.add('y') #Can add new elements easily
print set2

set3 = frozenset('lulzsec') #Cannot add new elements
print 'l' in set3 # Testing if element is present in a set, returns bool
print "No. of Elements in FrozenSet_set3 ==> {}".format(len(set3))

## Testing Complex Numbers data types
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






