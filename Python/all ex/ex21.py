def add(a, b):
    print("ADDING %f + %f" % (a, b))
    return a + b
def substract(a, b):
    print("SUBSTRACTING %f - %f" % (a, b))
    return a - b
def multiply(a, b):
    print("MULTIPLYING %f * %f" % (a, b))
    return a * b
def divide(a, b):
    print("DIVIDING %f / %f" % (a, b))
    return a / b


print("Let's do some math with just functions")

age = add(30,5)
height = substract(120, 50)
weight = multiply(60, 0.01)
iq = divide(250,3)

print("Age: %f, Height: %f, weight: %f, IQ: %f" % (age, height, weight, iq))

print("Here is puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("that becomes:", what,"Can you do it by hand??")
