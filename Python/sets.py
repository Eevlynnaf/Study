#sets are unordered collections of unique objects
#it doesnt return duplicates
#the elements of the set are in different places on memory

my_set = {1,2,3,4,5,5}
my_set.add(100)
print(my_set)
print(5 in my_set)
print(len(my_set))

print(list(my_set))     #converting the set into a list

new_set = my_set.copy()

#print(my_set[0])       #sets dont support indexing

my_list = [6,7,8,9,10]      #converting a list to a set
print(set(my_list))