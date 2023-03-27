# infinite loop
# i = 0
# while i < 50:
#   print(i)

i = 0
while i < 50:
    print(i)
    break

while i < 50:
    print(i)
    i += 1
else:
    print('Done')

my_list = [1,2,3]
for item in my_list:
    pint(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break
