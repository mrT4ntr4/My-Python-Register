##  Sets, FrozenSets and MultiSets
set1 = {1,2,3,1,2,5,2,8,}
print set1

set2 = set('hello')
set2.add('y') #Can add new elements easily
print set2

set3 = frozenset('lulzsec') #Cannot add new elements
print 'l' in set3 # Testing if element is present in a set, returns 'bool'
print 's' not in set3 # just opposite of 'in'
print "No. of Elements in FrozenSet_set3 ==> {}".format(len(set3))

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



set6 = set4 | set5
set6.add(60)
set6.add(70)
print set6
print len(set6) # duplicates not allowed in sets

# multisets.py

from collections import Counter
multisetCounter = Counter([1,1,2,3])
print multisetCounter

import multiset
s1 = multiset.Multiset('aab')
print s1
