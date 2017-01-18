from common_components.fileprocessing_framework import fileprocessing_module as File
from . import logging_methods as Log


def runapplication(sourcerootpath, destinationrootpath, deletemode):

	print "==========================================="

	initiallogs = Log.ApplicationLogs()
	finallogs = processsubfolder("!ROOT!", sourcerootpath, destinationrootpath, "", initiallogs, deletemode)
	finallogs.writelogs(destinationrootpath)





def processsubfolder(currentfoldername, sourcerootpath, destinationrootpath, currentsubfolder, logsstart, deletemode):

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

		if (directorylisting[itemname] == "Folder"):

			if itemname == "@eaDir":

				print "Found @eaDir in ", currentsubfolder
				currentlogs.logaction("Found @eaDir in " + targetfolderpath)

				targetpath = File.concatenatepaths(targetfolderpath, itemname)
				if deletemode == True:
					if File.deletefolder(targetpath) == True:
						currentlogs.logdelete("Successfully deleted " + targetpath)
					else:
						currentlogs.logdelete("Failed to delete " + targetpath)
				else:
					currentlogs.logdelete(targetpath + " NOT deleted")


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
				currentlogs = processsubfolder(itemname, sourcerootpath, destinationrootpath, newsubfolder, currentlogs,
																											deletemode)

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