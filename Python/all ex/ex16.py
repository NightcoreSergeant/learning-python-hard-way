from sys import argv

script, filename = argv

print("We're going to erase %s" % filename)
print("If you don't want that, hit CTRL-C")
print("If you do want that, hit ENTER.")

input("? ")

print("Openning file.....")
target = open(filename, "w")

print("Truncating the file....")
target .truncate()

print("Now write three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target .write(line1)
target .write("\n")
target .write(line2)
target .write("\n")
target .write(line3)
target .write("\n")

print("Now finally, we close it")
target .close()
