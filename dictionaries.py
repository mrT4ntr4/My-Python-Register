## Dictionaries

keyboard = {1:'CTRL', 2:'SHIFT', 4:'ENTER' }
print keyboard # lists contents of dictionary

print keyboard.values() # lists all values of all keys

### Accessing values

####  Using key
print keyboard[2] 
#### Using get()
print keyboard.get(2) 

print keyboard.keys() # gathers list all keys

### Deleting values

#### Using del
del keyboard[2] 

#### Using pop() 
#keyboard.pop(2) 

### Some Useful Built-In Functions

print keyboard.items() # returns a *list of dict's (key,value) tuple pairs

dup = keyboard.copy() # duplicates a predefined dict
print dup

print keyboard.has_key(2) # Checks for a key in dict, Return bool

keys = {1,2,3}
value = 'NUMPAD'

kb2 = dict.fromkeys(keys, value) # Using fromkeys to create a dict from a sequence
print(kb2)

print len(kb2) # Counts the no. of (key,value) pair

print cmp(dup,kb2)
# returns 0 if both dictionaries are equal, -1 if kb2 < dup and 1 if kb2 > dup.

keyboard.popitem() # pops out the first (key,value) pair
print keyboard

keyboard.clear() # Deletes every key,value pair present in the dictoinary
print keyboard



