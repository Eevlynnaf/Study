basket = [1,2,3,4,5]

new_list = basket.append(100)
#basket.insert(2, 300)
print(basket)
print(new_list)      #.append will add to the existing variable but will not give new results inside a new variable

basket.pop()
basket.remove(4)
print(basket)
basket.clear()
print(basket)

basket1 = ['a', 'b', 'c', 'd', 'e']

print(basket1.index('d', 0, 4))
print('d' in basket1)
print('x' in basket1)
print(basket1.count('d'))