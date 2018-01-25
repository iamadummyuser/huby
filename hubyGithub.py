#!/usr/bin/python
from github import Github


class hubyGithub(object):
    '''This Class aim is to interact with Github(Privatize the repos, list the repos) '''    
    def __init__(self):
        self.orgNames=[''] #Enter the organization or username
        self.orgSifre=[''] #Enter the Administarative Personal Access Key in order to privatize the public repos (OPTIONAL)
        self.dummyapi=''

    def getOrganization(self,orgname):
        repoNames=[]
        g=Github(self.dummyapi) #Dummy user API Key
        orgRepo=g.get_organization(orgname).get_repos()
        for repos in orgRepo:
            repoNames.append(repos.name)
        return repoNames

    def forkOrNot(self,orgname,reponame):
        g=Github(self.dummyapi) #Dummy user API Key
        temp=g.get_organization(orgname).get_repo(reponame)
        return temp.fork


    def privatizeOneRepo(self,orgname,reponame):
        g=Github(self.orgSifre[self.orgNames.index(orgname)])
        temp=g.get_organization(orgname).get_repo(reponame)
        temp.edit(private=True)

    def run(self):
        urllist=[]
        for orgs in self.orgNames:
            orgRepos=self.getOrganization(orgs)
            for repos in orgRepos:
                print repos
                if self.forkOrNot(orgs,repos):
                    print "is forked"
                    stringstyle='%s/%s'%(orgs,repos)
                    urllist.append(stringstyle)
                else:
                    print "is not forked"
                    self.privatizeOneRepo(orgs,repos)
        return urllist