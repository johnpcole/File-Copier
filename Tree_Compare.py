from codebase import main_application as TreeCompare

foldername = "Archive"
sourceroot = "/media/ubuntu/1.41.10-2228/" + foldername
targetroot = "/media/ubuntu/Other_Users/" + foldername


print "Application Started"
TreeCompare.runapplication("C:\\test1", "C:\\test2", False)
print "Application Ended"
