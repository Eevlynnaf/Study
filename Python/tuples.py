#tuples are like lists, but immutable

my_tuple = (1,2,3,4,5)

print(my_tuple[1])
print(5 in my_tuple)

print(my_tuple.count(4))
print(my_tuple.index(3))
print(len(my_tuple))

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z, *other = (5,6,7,8,9)
print(z)
print(other)