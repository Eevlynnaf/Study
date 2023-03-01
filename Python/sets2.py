my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
#print(my_set.discard(5))       #returns none
my_set.discard(5)
print(my_set)
my_set.difference_update(your_set)
print(my_set)
.intersection()
.isdisjoint()
.issubset()
.issuperset()
.union()