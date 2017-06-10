from sys import argv

script, filename = argv

target = open(filename, "w")

target .truncate()

line1= input('line1: ')
line2= input('line2: ')
line3= input('line3: ')

target.write("%s \n %s \n %s \n" % (line1,line2,line3))

target .close()
