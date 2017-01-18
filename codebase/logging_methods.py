from common_components.fileprocessing_framework import fileprocessing_module as File



class ApplicationLogs():
	def __init__(self):
		self.applog = ['Application Log', '==============================']
		self.errorlog = ['Error Log', '==============================']
		self.sourcefoldercount = 0
		self.targetfoldercount = 0
		self.sourcefilecount = 0
		self.targetfilecount = 0
		self.errorcount = 0


	def logaction(self, newentry):
		self.applog.append(newentry)



	def logerror(self, newentry):
		self.errorlog.append(newentry)



	def writelogs(self, destinationfolder):
		self.logaction('==============================')
		self.logcompletedfolder("TOTAL", "TOTAL", self.sourcefilecount, self.targetfilecount,
							self.sourcefoldercount, self.targetfoldercount, self.errorcount)


		self.logerror('==============================')
		File.writetodisk(File.concatenatepaths(destinationfolder, "Tree-Compare-Outcomes.log"), self.applog)
		File.writetodisk(File.concatenatepaths(destinationfolder, "Tree-Compare-Errors.log"), self.errorlog)



	def logcompletedfolder(self, currentfoldername, currentsubfolder, sourcefiles, targetfiles, sourcefolders,
																								targetfolders, errors):
		logvalue = " " * 50
		logvalue = logvalue + currentfoldername
		logvalue = logvalue[-50:]
		counter = "         " + str(sourcefolders - targetfolders)
		logvalue = logvalue + counter[-5:] + " folders (of"
		counter = "         " + str(sourcefolders)
		logvalue = logvalue + counter[-8:] + "),"
		counter = "         " + str(sourcefiles - targetfiles)
		logvalue = logvalue + counter[-5:] + " files (of"
		counter = "         " + str(sourcefiles)
		logvalue = logvalue + counter[-8:] + "),"
		counter = "         " + str(errors)
		logvalue = logvalue + counter[-6:] + " errors   " + currentsubfolder
		self.logaction(logvalue)

		self.sourcefoldercount = self.sourcefoldercount + sourcefolders
		self.targetfoldercount = self.targetfoldercount + targetfolders
		self.sourcefilecount = self.sourcefilecount + sourcefiles
		self.targetfilecount = self.targetfilecount + targetfiles
		self.errorcount = self.errorcount + errors

