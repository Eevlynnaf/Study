# enumerate is useful if you need the index counter of the item that you're looping through

for i, char in enumerate('Hellooo'):
    print(i, char)

for i, char in enumerate([1,2,3,4]):
    print(i, char)