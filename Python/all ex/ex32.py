the_count = [1,2,3,4]
fruits = ['apples', 'oranges', 'pears', 'bannana']
change = ['monaliza', True, 0.24, 53]

for number in the_count:
    print("Here are the numbers {}" .format(number))

for fruit in fruits:
    print("Here are fruits {}" .format(fruit))

for i in change:
    print("Here is change {}" .format(i))

for i in range(0, 6):
    print("adding to list fruits {}" .format(i))
    fruits.append(i)

for i in fruits:
    print("fruits were: {}" .format(i))
