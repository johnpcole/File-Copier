from common_components.fileprocessing_framework import fileprocessing_module as File
from . import filename_methods as FileName
from . import indexfile_methods as IndexFile
from . import nfooutput_methods as FileOutput


def runapplication(rootfolderpath):


	print "==========================================="

	rootfilelist = File.getfolderlisting(rootfolderpath)

	nfocount = 0

	rootitemnamelist = rootfilelist.keys()
	rootitemnamelist.sort()
	for rootitemname in rootitemnamelist:

		if rootfilelist[rootitemname] == "Folder":
			nfocount = processsubfolder(rootfolderpath, rootitemname, "", "", nfocount)

	print "==========================================="
	print str(nfocount) + " NFOs processed"
	print "==========================================="



def processsubfolder(parentfolderpath, subfoldername, setname, nameprefix, nfocount):

	newnfocount = nfocount
	subfolderpath = File.concatenatepaths(parentfolderpath, subfoldername)
	#print "==========================================="
	#print subfolderpath

	directorylisting = File.getfolderlisting(subfolderpath)
	itemnamelist = directorylisting.keys()
	itemnamelist.sort()

	movielist = {}

	# Determine what the current set is
	newsetname = IndexFile.determinemovieset(subfolderpath, setname)

	if newsetname != "":

		newnameprefix = IndexFile.determinenameprefix(subfolderpath, nameprefix)

		# Process Movies files if a multimovie folder
		multimovieflag = IndexFile.determinefoldertype(subfolderpath)
		if multimovieflag == True:
			for itemname in itemnamelist:
				if directorylisting[itemname] == "File":
					if FileName.getfiletype(itemname) == "Movie":
						sanitiseditemname = FileName.getsanitisedfilename(itemname)
						if sanitiseditemname in movielist.keys():
							print "     Duplicate movie name: ",sanitiseditemname , " ignored from ", itemname
						else:
							movielist[sanitiseditemname] = ""
							#print "     Multi Movie:", itemname, " captured as ", sanitiseditemname

		# Process single movie if at least one movie file present
		else:
			ismoviepresent = False
			for itemname in itemnamelist:
				if directorylisting[itemname] == "File":
					if FileName.getfiletype(itemname) == "Movie":
						ismoviepresent = True
			if ismoviepresent == True:
				movielist[subfoldername] = ""
				#print "     Single Movie:", subfoldername, " assumed "
			#else:
				#print "     Folder contains no movies"


		# Process Images
		for itemname in itemnamelist:
			if directorylisting[itemname] == "File":
				if FileName.getfiletype(itemname) == "Image":
					sanitiseditemname = FileName.getsanitisedfilename(itemname)
					if sanitiseditemname in movielist.keys():
						movielist[FileName.getsanitisedfilename(itemname)] = itemname
						#print "     Image:", itemname, " captured for ", sanitiseditemname
					#else:
						#print "     Ignored Image:", itemname


		# Write NFOs
		newnfocount = FileOutput.outputnfos(subfolderpath, movielist, newsetname, newnameprefix, newnfocount)


		# Process subfolders
		for itemname in itemnamelist:
			if directorylisting[itemname] == "Folder":
				newnfocount = processsubfolder(subfolderpath, itemname, newsetname, newnameprefix, newnfocount)


	return newnfocount