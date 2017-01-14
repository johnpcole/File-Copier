from common_components.fileprocessing_framework import fileprocessing_module as File



def outputnfos(folderpath, movielist, setname, nameprefix, nfocount):

    newnfocount = nfocount
    movienamelist = movielist.keys()
    movienamelist.sort()
    for moviename in movienamelist:
        newnfocount = newnfocount + 1
        filepath = createfilepath(folderpath, moviename)
        fileoutput = createnfocontent(nameprefix + moviename, movielist[moviename], setname)

        decision = checkexistingnfo(folderpath, moviename, setname, nameprefix, movielist[moviename])

        if decision == "Missing":
            messageprefix = "          Creating new file "
        elif decision == "Already Up To Date":
            messageprefix = "Not modifying existing file "
        elif decision == "Out Of Date":
            messageprefix = "     Updating existing file "
        else:
            messageprefix = "    Unknown action for file "

        outputmessage = messageprefix + str(nfocount).zfill(4) + ": " + filepath

        if movielist[moviename] == "":
            outputmessage = outputmessage + ".........................................................................."
            outputmessage = outputmessage + ".........................................................................."
            outputmessage = outputmessage[:150] + "[No Image]"


        print outputmessage
        if (decision == "Out Of Date") or (decision == "Missing"):
            File.writetodisk(filepath, fileoutput)


    return newnfocount



def createnfocontent(moviename, imagename, setname):

    fileoutput = []
    fileoutput.append("<movie>")
    fileoutput.append("\t<title>" + moviename + "</title>")
    fileoutput.append("\t<set>" + setname + "</set>")
    if imagename != "":
        fileoutput.append("\t<thumb>" + imagename + "</thumb>")
    fileoutput.append("</movie>")

    return fileoutput



def createfilepath(folderpath, moviename):

    return File.concatenatepaths(folderpath, moviename + ".nfo")



def checkexistingnfo(folderpath, moviename, setname, nameprefix, imagename):

    outcome = "Missing"

    nfofilepath = createfilepath(folderpath, moviename)
    if File.doesexist(nfofilepath):
        olddata = File.readfromdisk(nfofilepath)
        newdata = createnfocontent(nameprefix + moviename, imagename, setname)
        if len(olddata) == len(newdata):
            outcome = "Already Up To Date"
            for index in range(0, len(olddata)):
                if olddata[index] != newdata[index]:
                    outcome = "Out Of Date"
        else:
            outcome = "Out Of Date"

    return outcome