from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying file %s to file %s" % (from_file, to_file))

# can make 1 line here but how
in_file = open(from_file)
blabla = in_file .read()

print("This file is %s bytes long" % len(blabla))

print("Does output file exists? %r" % exists(to_file))

out_file = open(to_file, "w")
out_file .write(blabla)

print("Done!")

out_file .close()
in_file .close()
