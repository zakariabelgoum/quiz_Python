################ code by Zakaria Belgoum #############

def sort_tuple(my_tuple):
	''' this function sort tuples 
	sort_tuple((5,2))= (2,5)
	sort_tuple((1,2))=(1,2) '''
	sortedtuple=sorted(my_tuple)
	return sortedtuple


def isOverlap(input1,input2):
	''' input1 and input2 should be firstly sorted 
	there is overlap when the first element of one of the inputs is between the two elements of the other input '''
	sortedInput1=sort_tuple(input1)
	sortedInput2=sort_tuple(input2)
	if    sortedInput1[0] <=sortedInput2[0]<= sortedInput1[1] or sortedInput2[0] <=sortedInput1[0]<= sortedInput2[1]:
		print(' %s and %s overlaps '%(input1,input2))

	else :
		print(' %s and %s doesnt overlap '%(input1,input2))

#testing
isOverlap((1,2),(1,3))
isOverlap((2,5),(1,3))
isOverlap((9,5),(10,12))












