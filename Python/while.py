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