from sys import argv #importa

script, input_file = argv #dobi argumente

def print_all(f): #nrdi funkcijo print_all: kar ji das to ti reada in pol sprinta
    print(f .read())

def rewind(f): #nrdi funkcijo rewind kar ji das ti da na zacetek za brat
    f .seek(0)

def print_a_line(line_count, f): #funkcijo k das spremenljivko in reda isto vrstico
    print(line_count, f .readline())

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
