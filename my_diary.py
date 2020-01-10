import sys
import datetime
from sys import argv

script, filename = argv


while True:
	print " "
	print "We're going to edit %r." % filename
	print '''If you don't want that,write "no" .'''
	print "If you do want that, hit 'yes'."
	print 'If you do want just read your %r write "read".' % filename

	choice = raw_input()
	if choice == "no":
		sys.exit()
	elif choice == "read":
		diary = open(filename,'r')
		print diary.read()
		diary.close()
	elif choice == "yes":
		target = open(filename,'r+')
		reads = target.read()
		target.close()
		target = open(filename,'w+')
		print "You can write something in your diary"
		print "Write:"

		line = raw_input()
		d = len(line)
		print "I'm going to write these to the file."

		if len(reads) == 0:
			target.write("-"*10)
			target.write('My Diary')
			target.write("-"*10)
			target.write("\n")

		target.write(reads)
		target.write(str(datetime.date.today()))
		target.write(':')
		target.write("\n")
		target.write("-" * d)
		target.write("\n")
		target.write(line)
		target.write("\n")
		target.write("-" * d)
		target.write("\n")
		
		
		target.close()