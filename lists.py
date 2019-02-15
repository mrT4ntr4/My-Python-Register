
list = [11,22,11,'hello']
list.append('22') # appending single element
print list

list.extend([55,'world'])  # appending more than 2 elements
print list

list.insert(1, 'MyList') # adding new element at a specific index
print list

print list[0:3] # Outputs first 3 elements

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

list3.pop(6)  # Removes element at index 6
print list3

print list3.count(3) # Counts no. of times 3 appears

list3.reverse() # Reverses a list using function
print list3

print list1[::-1]  # Reverse a list by Slicing

for number in list3: # Iterating through a list
	print (number), 

