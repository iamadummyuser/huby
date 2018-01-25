#!/usr/bin/python
import os


class hubyFile(object):
    '''This Class aim is to interact with files(clone,crawl,read,delete) '''    
    def __init__(self):
        print 'Hello'

    def list_files(self,startpath):
        fileTree=[]
        for root, dirs, files in os.walk(startpath):
            for f in files:
                tempFileTree="%s/%s"%(root,f)
                fileTree.append(tempFileTree)
        return fileTree

    def openFiles(self,filePath):
        with open(filePath) as filep:
            fp=filep.readlines()
        return fp


    def cloneRepo(self,repourl):
        os.system("mkdir /tmp/repositories")
        os.system("mkdir /var/RepositoryAnalysis")
        os.system("touch /var/RepositoryAnalysis/%s.html"%(repourl.split('/')[1]))
        os.system("cd /tmp/repositories && git clone https://github.com/"+repourl+".git")

    def removeRepo(self,reponame):
        print 'Removing repo : '+reponame
        os.system('rm -rf '+reponame+'/')

    def cleanup(self):
        os.system('rm -rf /tmp/repositories/')