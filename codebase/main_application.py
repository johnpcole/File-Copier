from common_components.fileprocessing_framework import fileprocessing_module as File


def runapplication(sourcerootpath, destinationrootpath):

	print "==========================================="

	processsubfolder(sourcerootpath, destinationrootpath, "", 0)


def processsubfolder(sourcerootpath, destinationrootpath, currentsubfolder, sublevel):

	sourcefolderpath = File.concatenatepaths(sourcerootpath, currentsubfolder)
	targetfolderpath = File.concatenatepaths(destinationrootpath, currentsubfolder)

	directorylisting = File.getfolderlisting(sourcefolderpath)
	itemnamelist = directorylisting.keys()
	itemnamelist.sort()

	# Process subfolders and files
	for itemname in itemnamelist:

		if (directorylisting[itemname] == "Folder") and (itemname != "@eaDir"):

			newsubfolderpath = File.concatenatepaths(targetfolderpath, itemname)
			File.makefolder(newsubfolderpath)

			newsubfolder = File.concatenatepaths(currentsubfolder, itemname)
			indenter = " " * sublevel
			print "     ", indenter, itemname
			processsubfolder(sourcerootpath, destinationrootpath, newsubfolder, sublevel + 1)

		elif directorylisting[itemname] == "File":

			sourcefile = File.concatenatepaths(sourcefolderpath, itemname)
			targetfile = File.concatenatepaths(targetfolderpath, itemname)
			File.copyfile(sourcefile, targetfile)

		else:
			assert directorylisting[itemname] == "Folder", "Unknown File System Object Type"


	return