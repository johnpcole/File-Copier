from common_components.fileprocessing_framework import fileprocessing_module as File
from . import logging_methods as Log


def runapplication(sourcerootpath, destinationrootpath):

	print "==========================================="

	initiallogs = Log.ApplicationLogs()
	finallogs = processsubfolder("!ROOT!", sourcerootpath, destinationrootpath, "", initiallogs)
	finallogs.writelogs(destinationrootpath)





def processsubfolder(currentfoldername, sourcerootpath, destinationrootpath, currentsubfolder, logsstart):

	currentlogs = logsstart

	sourcefolderpath = File.concatenatepaths(sourcerootpath, currentsubfolder)
	targetfolderpath = File.concatenatepaths(destinationrootpath, currentsubfolder)

	directorylisting = File.getfolderlisting(sourcefolderpath)
	itemnamelist = directorylisting.keys()
	itemnamelist.sort()
	sourcefilecount = 0
	sourcefoldercount = 0
	targetfilecount = 0
	targetfoldercount = 0

	errorcount = 0

	# Process subfolders and files
	for itemname in itemnamelist:

		if (directorylisting[itemname] == "Folder") and (itemname != "@eaDir"):

			if itemname == "@eaDir":

				print "Found @eaDir at ", currentsubfolder

			else:

				sourcefoldercount = sourcefoldercount + 1

				targetpath = File.concatenatepaths(targetfolderpath, itemname)
				if File.doesexist(targetpath) == True:
					targetfoldercount = targetfoldercount + 1
				else:
					currentlogs.logerror("Cannot see Folder - " + targetpath)
					errorcount = errorcount + 1

				newsubfolder = File.concatenatepaths(currentsubfolder, itemname)
				print newsubfolder
				currentlogs = processsubfolder(itemname, sourcerootpath, destinationrootpath, newsubfolder, currentlogs)

		elif directorylisting[itemname] == "File":

			sourcefilecount = sourcefilecount + 1

			targetpath = File.concatenatepaths(targetfolderpath, itemname)
			if File.doesexist(targetpath) == True:
				targetfilecount = targetfilecount + 1
			else:
				currentlogs.logerror("Cannot see File - " + targetpath)
				errorcount = errorcount + 1

		else:
			assert directorylisting[itemname] == "Folder", "Unknown File System Object Type"

	currentlogs.logcompletedfolder(currentfoldername, currentsubfolder, sourcefilecount, targetfilecount,
																	sourcefoldercount, targetfoldercount, errorcount)

	return currentlogs