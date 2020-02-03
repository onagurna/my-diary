import sys
import time
import datetime
from sys import argv

script, filename = argv


while True:
	print " "
	print "We're going to edit %r." % filename
	print '''If you don't want that,write "no" .'''
	print "If you do want that, hit 'yes'."
	print 'If you do want just read your %r write "read".' % filename
	print 'If you do want find note from some day write "find"'

	choice = raw_input()
	if choice == "no":
		sys.exit()


	elif choice == "find":
		target = open(filename,'r+')
		reads = target.read()
		target.close()
		print'Now write this date like year(2020)-mounth(01)-day(01)'
		note = raw_input()
		result_date = reads.find(note)
		end = reads.find("-"*17)
		if result_date != -1 and end != -1:
			inf = reads[result_date:end]
			print inf
		elif result_date != -1 and end == -1:
			inf = reads[result_date:-1]
			print inf
		elif result_date == -1:
			print "No data"

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
		d_len = len(line)
		print "I'm going to write these to the file."

		if len(reads) == 0:
			title = ("-"*10+'My Diary'+"-"*10 +"\n")
			target.write(title)
		
		target.write(reads)
		named_time = time.localtime()
		time_string = time.strftime("%H:%M", named_time)
		date = str(datetime.date.today())
		result = reads.find(date)
		if result == -1:
			if len(reads) != 0:
				target.write("-"*17)
			target.write(date +':'+"\n")
		target.write("-"*10+time_string+"-"*10 +"\n"+line+"\n")
		
		target.close()