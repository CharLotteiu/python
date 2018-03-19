# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import re  
import collections  
  
''''' 
从文件中读取内容，统计词频 
'''   
wordlist={}
text=[]
all_the_text=""
path=""

for i in range(5):
    path = str(i+1) + '.txt'
    f = open(path)
    text.append(f.read())

for x in text:
    all_the_text += x
    
all_the_text = all_the_text.lower() 
all_the_text = re.sub("\"|,|\.|\”", "", all_the_text)

for word in all_the_text.split():  
            if word not in wordlist:  
                wordlist[word] = 0  
            wordlist[word] += 1

wordlist = collections.OrderedDict(sorted(wordlist.items(), key = lambda t: -t[1]))
            
print "词频最高Top 10"
print "freq*	word\n"
print "-----   -----\n"

j=0
for key,value in wordlist.items():
    if j<10:
        print ("%-7d %-7s" % (value,key))
        j=j+1
    else:
        break
    
wordlist1 = collections.OrderedDict(sorted(wordlist.items(), key = lambda t: t[1]))

print "\n词频最低Top 10"
print "freq*	word\n"
print "-----   -----\n"

j=0
for key,value in wordlist1.items():
    if j<10:
        print ("%-7d %-7s" % (value,key))
        j=j+1
    else:
        break