################ code by Zakaria Belgoum ###############
# we suppose that (x1,x2),(x3,x4) are two sorted tuples
# (x1,x2) and (x3,x4) overlaps when x3 <= x1 <= x4 or x1 <= x3 <= x2
########################################################


def sort_tuple(my_tuple):
	sortedtuple=sorted(my_tuple)
	return sortedtuple


def is_overlap(input1,input2):
	sortedInput1=sort_tuple(input1)
	sortedInput2=sort_tuple(input2)
	if sortedInput1[0] <=sortedInput2[0]<= sortedInput1[1] or sortedInput2[0] <=sortedInput1[0]<= sortedInput2[1]:
		return '{} and {} overlaps'.format(input1,input2)
	else :
		return '{} and {} doesnt overlap'.format(input1,input2)



if __name__ == "__main__":
	print(is_overlap((1,2),(1,3)))
	print(is_overlap((9,5),(10,12)))












