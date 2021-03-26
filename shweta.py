def myhisto( items ): # create function
	for n in items: # for loop through values of n
		output = ''
		times = n
		while( times > 0 ): # check condition of counter
			output += '*'
			times = times  -1 # decrement the counter
		print(output) # print the out pu

myhisto([1,2, 3, 6, 5,10,6])	
