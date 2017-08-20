import numbers
"""
	Multiline comment starts 

		This creates a function, that takes one input number 
		and prints the factorial of that number.

	Multiline comment ends
"""

def get_me_factorial(toFact):
	fact = 1
	loopCounter = toFact
	if isinstance(toFact, int) == True: 
		while (loopCounter > 0): 
			fact = loopCounter * fact
			loopCounter = loopCounter -1
		print fact
	else: print "please enter an integer"


"""
	There's one problem with the above program. 
	In case if the user intends to send a number as string like '3', it won't 
	consider, rather it treats as string
"""
