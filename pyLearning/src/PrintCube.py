import numbers
"""
	Multiline comment starts 

		This sample program aims to print cube of a given input
		In case if the user inputs anything other than number, it prints
			do give proper input

	Multiline comment ends
"""

def get_me_cube(prime):
	if isinstance(prime, numbers.Real) == True: print prime**3
	else: print "please enter a real number"


"""
	There's one problem with the above program. 
	In case if the user intends to send a number as string like '3', it won't 
	consider, rather it treats as string
"""
