from common_components.fileprocessing_framework import fileprocessing_module as File



def determinemovieset(subfolderpath, existingsetname):

	indexfilepath = File.concatenatepaths(subfolderpath, "_index_.set")
	if File.doesexist(indexfilepath):
		outcome = "-"
		filecontents = File.readfromdisk(indexfilepath)
		for lineitem in filecontents:
			if lineitem != "":
				outcome = lineitem
	else:
		outcome = existingsetname

	return outcome



def determinenameprefix(subfolderpath, existingprefix):

	indexfilepath = File.concatenatepaths(subfolderpath, "_index_.prefix")
	if File.doesexist(indexfilepath):
		outcome = "-"
		filecontents = File.readfromdisk(indexfilepath)
		for lineitem in filecontents:
			if lineitem != "":
				outcome = lineitem
	else:
		outcome = existingprefix

	return outcome



def determinefoldertype(subfolderpath):

	return File.doesexist(File.concatenatepaths(subfolderpath, "_index_.multimovie"))

