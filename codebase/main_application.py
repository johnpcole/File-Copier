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
	filecount = 0
	foldercount = 0
	errorcount = 0

	# Process subfolders and files
	for itemname in itemnamelist:

		if (directorylisting[itemname] == "Folder") and (itemname != "@eaDir"):

			newsubfolderpath = File.concatenatepaths(targetfolderpath, itemname)
			if File.makefolder(newsubfolderpath) == True:
				foldercount = foldercount + 1
			else:
				currentlogs.logerror("Cannot Make Folder - " + newsubfolderpath)
				errorcount = errorcount + 1

			newsubfolder = File.concatenatepaths(currentsubfolder, itemname)
			print newsubfolder
			currentlogs = processsubfolder(itemname, sourcerootpath, destinationrootpath, newsubfolder, currentlogs)

		elif directorylisting[itemname] == "File":

			sourcefile = File.concatenatepaths(sourcefolderpath, itemname)
			targetfile = File.concatenatepaths(targetfolderpath, itemname)
			if File.copyfile(sourcefile, targetfile) == True:
				filecount = filecount + 1
			else:
				currentlogs.logerror("Cannot Copy File - " + targetfile)
				errorcount = errorcount + 1

		else:
			assert directorylisting[itemname] == "Folder", "Unknown File System Object Type"

	currentlogs.logcompletedfolder(currentfoldername, currentsubfolder, filecount, foldercount, errorcount)

	return currentlogs