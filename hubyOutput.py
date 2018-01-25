#!/usr/bin/python
import datetime

class hubyOutput(object):
    '''This Class aim is to create a human readable form in HTMl'''    
    def __init__(self):
        self.currentrepo=''
        self.finalhtml=[]

    def testprint(self,filename,findings):
        print filename
        print findings
    def start(self,reponame):
        self.currentrepo=reponame
        consthtmlone='<html><head><title>%s</title><style>div{background-color: lightgrey;}</style></head><body>'%(self.currentrepo)
        contentbegin='<h1>%s</h1><h3>Last Analyzed: %s</h3><hr/>'%(self.currentrepo,datetime.datetime.now())
        self.finalhtml.append(consthtmlone)
        self.finalhtml.append(contentbegin)

    def writeToFile(self):       
        htmlfile=open("/var/RepositoryAnalysis/%s.html"%(self.currentrepo.split('/')[1]),'w')
        for html in self.finalhtml:
            htmlfile.write(html)
        htmlfile.close()



    def preparediv(self,filename,findings):
        self.finalhtml.append('<h2>Location: '+filename+'</h2>')
        for f in findings:
            tempdiv='<div><p>%s</p></div>'%(unicode(f,errors='ignore'))
            self.finalhtml.append(tempdiv)

    def end(self):
        consthtmltwo='</body></html>'
        self.finalhtml.append(consthtmltwo)
        self.writeToFile()


    def cleanuphtml(self):
        self.finalhtml=[]
        self.currentrepo=''
