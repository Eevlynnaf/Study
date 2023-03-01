#dictionary is an unordered key value pair
#the key needs to be immutable and unique

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['b'])
print(dictionary.get('age'))
print('a' in dictionary.keys())
print(dictionary.items())

#dictionary.clear()
#print(dictionary)
#dictionary2 = dictionary.copy()
#dictionary.pop('2')
#dictionary.update({'a': 55})

user = dict(name='JohnJohn')
print(user)
print('JohnJohn' in user)
print('JohnJohn' in user.values())