from sys import argv

script, filename = argv

txt = open(filename)

print("Here is your file {}:" .format(filename))
print(txt .read())

print("Type the filename again:")
file_again = input("> ")

txt_again = close(open(file_again))

print(txt_again.read())
