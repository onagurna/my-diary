import sys
from sys import argv
import time

script, filename = argv

print "We're going to edit %r." % filename
print '''If you don't want that,write "no" .'''
print "If you do want that, hit Enter."
print 'If you do want just read your %r write "read".' % filename
choice = raw_input()

# if choice == "no":
# 	sys.exit()
# elif choice == "read":
# 	diary = open(filename,'r')
# 	print diary.read()
# 	diary.close()
# 	sys.exit()


target = open(filename,'w+')
reads = target.read()
#target.write(reads)
print'reads: '+ reads

print "You can write something in your diary"
print "Write:"
line = raw_input()
d = len(line)

print "I'm going to write these to the file."
#reads = target.read()
#target.write(reads)
#print'reads: '+ reads
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