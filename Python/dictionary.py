#dictionary is an unordered key value pair
#the key needs to be immutable and unique

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['b'])
print(dictionary.get('age'))

user = dict(name='JohnJohn')
print(user)
print('JohnJohn' in user)