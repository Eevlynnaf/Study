#iterable - lists, dictionary, tuple, set, string
# these can be iterated - go one by one and check each item in the collection

user = {
    'name' : 'Golem',
    'age' : 5006,
    'can_swim' : False
}

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)