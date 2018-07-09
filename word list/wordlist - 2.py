# -*- coding: utf-8 -*-
"""
@author: Charlotte
"""

import re, os 
import collections   

class Tongjicipin:
    
    def __init__(self):
        self.wordlist={}
        self.text=[]
        self.all_the_text=""
        
    def duquwenjian(self,files):
        for file in files:
            filepath = file
            for line in open(filepath,'r',encoding='UTF-8'):
                self.text.append(line)
                    
    def list2string(self):
        for x in self.text:
            self.all_the_text += x
            
    def standerize(self):
        self.all_the_text = self.all_the_text.lower() 
        self.all_the_text = re.sub("\"|,|\.|\”", "", self.all_the_text)
        
    def frequency(self):
        for word in self.all_the_text.split():  
            if word not in self.wordlist:  
                self.wordlist[word] = 0  
            self.wordlist[word] += 1
    
    def Top10(self):
        wordlist = collections.OrderedDict(sorted(self.wordlist.items(), key = lambda t: -t[1]))
        print ("\n词频最高Top 10")
        print ("freq*	word\n")
        print ("-----   -----\n")
        j=0
        for key,value in wordlist.items():
            if j<10:
                print ("%-7d %-7s" % (value,key))
                j=j+1
            else:
                break
    
    def Last10(self):
        wordlist = collections.OrderedDict(sorted(self.wordlist.items(), key = lambda t: t[1]))

        print ("\n词频最低Top 10")
        print ("freq*	word\n")
        print ("-----   -----\n")
        
        j=0
        for key,value in wordlist.items():
            if j<10:
                print ("%-7d %-7s" % (value,key))
                j=j+1
            else:
                break
            
    def run(self,files):
        self.duquwenjian(files)
        self.list2string()
        self.standerize()
        self.frequency()
        self.Top10()
        self.Last10()

def main():
    tongjicipin = Tongjicipin()
    files=[]
    filedir = os.getcwd()+'/corpara'
    filenames=os.listdir(filedir)
    for filename in filenames:
        file = filedir + '/' + filename
        files.append(file)
    tongjicipin.run(files)
    
main()