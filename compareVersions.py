################### code by Zakaria Belgoum #############

###################Code by Zakaria Belgoum ################3


from packaging import version

def compareVersionString(str1,str2):

	#version.parse(stringObject) converts a string object into a version object
	if version.parse(str1) < version.parse(str2):
		print('%s is greater than %s'%(str2,str1))

	elif version.parse(str1) > version.parse(str2):
		print('%s is greater than %s'%(str1,str2))


	elif version.parse(str1) == version.parse(str2):
		print('%s is equal to %s'%(str1,str2))


compareVersionString('Äú1.2‚Ä','Äú1.2‚Äa')




