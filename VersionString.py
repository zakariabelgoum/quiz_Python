############ Code by Zakaria Belgoum ################
#compare two version strings version1 and version2
#the . is used to separate version sequences 
####################################################


class VersionString(object):

	def compare_version(self,version1,version2):
		version1_list = version1.split('.')
		version2_list = version2.split('.')
		if len(version1_list) > len(version2_list):
			version2_list += ['0' for _ in range(len(version1_list)-len(version2_list))]
		elif len(version2_list) > len(version1_list):
			version1_list += ['0' for _ in range(len(version2_list)-len(version1_list))]
		i=0
		while i <= len(version1_list):
			if version1_list[i] > version2_list[i]:
				return '{} is greater than {} '.format(version1,version2)
			elif version1_list[i] < version2_list[i]:
				return '{} is greater than {} '.format(version2,version1)
			else:
				i += 1

if __name__=="__main__" :
	print(VersionString().compare_version('1.2.2','1.2.3'))
	print(VersionString().compare_version('1.2,2','1.2,a'))
	print(VersionString().compare_version('abc.A','abc.B'))
	print(VersionString().compare_version('Äú1.2‚Äù','Äú1.1‚Äù'))
	
	

