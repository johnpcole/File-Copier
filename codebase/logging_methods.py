from common_components.fileprocessing_framework import fileprocessing_module as File

class ApplicationLogs():

    def __init__(self):
        self.applog = ['Application Log', '==============================']
        self.errorlog = ['Error Log', '==============================']

    def logaction(self, newentry):
        self.applog.append(newentry)

    def logerror(self, newentry):
        self.errorlog.append(newentry)

    def writelogs(self, destinationfolder):
        self.logaction('==============================')
        self.logerror('==============================')
        File.writetodisk(File.concatenatepaths(destinationfolder, "File-Copier-Actions.log"), self.applog)
        File.writetodisk(File.concatenatepaths(destinationfolder, "File-Copier-Errors.log"), self.errorlog)



    def logcompletedfolder(self, currentfoldername, currentsubfolder, files, folders, errors):

        logvalue = " " * 50
        logvalue = logvalue + currentfoldername
        logvalue = logvalue[-50:]
        counter = "     " + str(folders)
        logvalue = logvalue + counter[-5:] + " folders,"
        counter = "     " + str(files)
        logvalue = logvalue + counter[-5:] + " files,"
        counter = "     " + str(errors)
        logvalue = logvalue + counter[-5:] + " errors   " + currentsubfolder
        self.logaction(logvalue)
