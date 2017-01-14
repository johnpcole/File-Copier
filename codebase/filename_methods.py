from common_components.fileprocessing_framework import fileprocessing_module as File



def getfiletype(filename):

	fileend = File.getextension(filename)
	fileend = fileend.lower()
	outcome = "Unknown"

	filetype = {}
	filetype['Movie'] = ['mp4', 'wmv', 'webm', 'vob', 'ts', 'rmvb', 'rm', 'mpg', 'mpeg', 'mov', 'mkv', 'm4v',
																				'iso', 'flv', 'divx', 'avi', 'asf']
	filetype['Image'] = ['jpg', 'gif', 'png', 'bmp']
	#filetype['NFO'] = ['nfo']


	for filetypeitem in filetype.keys():
		for matchitem in filetype[filetypeitem]:
			if fileend == matchitem:
				outcome = filetypeitem

	return outcome



def getsanitisedfilename(rawfilename):

	filename = File.getname(rawfilename)
	searchname = filename.lower()

	if ("-dvd" in searchname):
		filenamesplit = filename.split("-dvd")
		outcome = filenamesplit[0]

	elif ("- dvd" in searchname):
		filenamesplit = filename.split("- dvd")
		outcome = filenamesplit[0]

	else:
		outcome = filename


	return outcome
