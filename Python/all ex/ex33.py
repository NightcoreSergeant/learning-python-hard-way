i = 0
mylist = []
def whileloop(a, x):
    global i
    while i < a:
        print("I is now {}" .format(i))
        mylist.append(i)
        i += x
        print("my list now:", mylist)
        print("At the bottom of i is{}" .format(i))

print("The numbers:")

for num in mylist:
    print(num)



whileloop(100, 1)

mylist1 = []

def forloop(a, x, c):
    for i in range(a, x, c):
        print("this is i now: {}" .format(i))
        mylist1.append(i)
        print("mylist1=", mylist1)

forloop(0, 102, 2)
