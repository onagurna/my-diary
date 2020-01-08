import sys
from sys import argv
import time

script, filename = argv

print "We're going to erase %r." % filename
print '''If you don't want that,write "no" .'''
print "If you do want that, hit Enter."
choice = raw_input("?")
if choice == "no":
	sys.exit()

print "Opening the file..."
target = open(filename, 'a')

print "You can write something"

line = raw_input("Write:")

print "I'm going to write these to the file."

target.write(time.asctime())
target.write(':  ')
target.write(line)
target.write("\n")

print "And finally, we close it."
target.close()