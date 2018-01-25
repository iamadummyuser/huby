#!/usr/bin/python
import string as st

class hubySearch(object):
    '''This Class aim is to search the keywords on the lists and create an output list with findings '''    
    def __init__(self,wordlist):
        self.searchList=[]
        self.transDict={}
        self.buildTfunc(wordlist)

    def string_matching_FSM(self,T, trans, m):
        """
        T: is the input Line;
        trans: is the transition function that define the pattern P we need to look
        for;
        m: lenght of the pattern
        cnt : Line count
        """
        try:
            T=T.lower()
        except:
            pass
        s = 0
        for i,c in enumerate(T):
            try:
                s = trans[s][c]
                if s == m:
                    return True
            except:
                pass
        return False

    def transition_function(self,P):
        """
        The main principle on building the transition function is to think about
        the fact that every time we scan a new character from the input sequence
        the suffix should match with the prefix of the pattern. If that is not
        possible for every length of the suffix, the next state need to be the
        initial, otherwise the length of the suffix that matches properly will be
        exactly the next state.
        """
        alphabet = st.printable
        m = len(P)
        trans = [{c:0 for c in alphabet} for i in range(m)]
        for s in range(m):
            for c in alphabet:
                k = min(m, s+1)
                while (P[:s]+c)[-k:] != P[:k]:
                    k-=1

                trans[s][c]=k
        return trans


    def buildTfunc(self,wordlist):
        for i in wordlist:
            self.transDict[i]=self.transition_function(i)

    def searchThread(self,searchKey):
        findings=[]
        getList=self.searchList
        for lines in getList:
            if self.string_matching_FSM(lines,self.transDict[searchKey],len(searchKey)):
                findings.append(lines)
            else:
                pass
        return findings

    def getSearchList(self,liste):
        self.searchList=liste

