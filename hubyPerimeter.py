#!/usr/bin/python
import hubyFile
import hubyGithub
import hubySearch
import hubyOutput
from pathos.multiprocessing import ProcessingPool

class hubyPerimeter(object):
    '''This class is the main class to control whole tool'''
    def __init__(self):
        self.wordlist=['api', 'key', 'username', 'user', 'uname', 'pw', 'password','pass', 'email', 'mail', 'credentials', 'credential', 'login', 'token', 'secret','e-mail','user name','vpn','creds']
        self.hFile=hubyFile.hubyFile()
        self.hGithub=hubyGithub.hubyGithub()
        self.hSearch=hubySearch.hubySearch(self.wordlist)
        self.hOutput=hubyOutput.hubyOutput()

    def run(self):
        urlToAnalyze=self.hGithub.run()                 #In order to analyze only one repo, comment this line and:
        #urlToAnalyze=['iamadummyuser/huby']            #please uncomment this line & enter the URL of the repo without github.com/
        for repositories in urlToAnalyze:
            filelist=[]
            self.hFile.cloneRepo(repositories)
            self.hOutput.start(repositories)
            repopwd="/tmp/repositories/"+repositories.split("/")[1]
            filelist=self.hFile.list_files(repopwd)
            for files in filelist:
                self.hSearch.getSearchList(self.hFile.openFiles(files))
                findingstemp=ProcessingPool().map(self.hSearch.searchThread,self.wordlist)#In case of cPickle Error https://github.com/uqfoundation/pathos/issues/121
                findlist=[]
                for findings in findingstemp:
                    if not findings:
                        continue
                    else:
                        for findtemp in findings:
                            findlist.append(findtemp)
                findset=set(findlist)
                if not findset:
                    continue
                else:
                    self.hOutput.preparediv(files,findset)
            self.hOutput.end()
            self.hOutput.cleanuphtml()
            self.hFile.removeRepo(repopwd)
        self.hFile.cleanup()

if __name__=="__main__":
    obje=hubyPerimeter()
    obje.run()