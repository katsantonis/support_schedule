#!/usr/bin/env python
from config import days
from config import weekend
from config import users
from config import vardies
from config import days2Nums

in_file = "input_test"

def readInput(filename):
	availabilities = []
	for i in range(17):
		availabilities.append( [] )	
	current_user   = ""
	current_day    = ""
	current_vardia = 0

	with open(filename) as f:

		for line in f:
			l = line.strip()
			if l in days:
				current_day = l
			else:
				words = l.split()
				for word in words:
					if word in users :
						current_user = word
						if current_day == "Saturday":
							availabilities[15].append(current_user)
						elif current_day == "Sunday":
							availabilities[16].append(current_user)
					if word in vardies:
						vardia = int(word)
						availabilities[3*days2Nums[current_day]+vardia -1 ].append( current_user )



	return availabilities


def avBucketCreator(availabilities):
	buckets = {}
	for av in availabilities:
		day = av[0]
		if day in weekend:
			if day in buckets:
				buckets[day] += 1
			else:
				buckets[day] = 1

		elif day in days:
			vardia = av[1]
			key = day + vardia
			if key in buckets:
				buckets[key] += 1
			else:
				buckets[key] = 1
		else:
			print "Error"
			sys.exit(2)

	return buckets.items()


		
		
