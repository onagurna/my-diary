import sys
from datetime import date
from sys import argv
import time

script, filename = argv

print "We're going to edit %r." % filename
print '''If you don't want that,write "no" .'''
print "If you do want that, hit Enter."
print 'If you do want just read your %r write "read".' % filename
choice = raw_input()

if choice == "no":
	sys.exit()
elif choice == "read":
	diary = open(filename,'r')
	print diary.read()
	diary.close()
	sys.exit()


target = open(filename,'r+')
reads = target.read()
#print'reads: '+ reads
target.close()
target = open(filename,'w+')

print "You can write something in your diary"
print "Write:"
line = raw_input()
d = len(line)

print "I'm going to write these to the file."
#print reads
#print len(reads)
if len(reads) == 0:
	target.write("-"*10)
	target.write('My Diary')
	target.write("-"*10)
	target.write("\n")
target.write(reads)
target.write(time.asctime())
target.write(':')
target.write("\n")
target.write("-" * d)
target.write("\n")
target.write(line)
target.write("\n")
target.write("-" * d)
target.write("\n")


target.close()