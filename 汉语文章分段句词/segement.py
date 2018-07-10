# -*- coding: utf-8 -*-
"""
@author: Charlotte
"""

import jieba
from snownlp import SnowNLP

text=""

f = open('corpus.txt','r')
text=f.read()

def cutparagraph(text):
    paragraphslist = list()
    print('以下是自行编写分段结果：\n')
    for paragraph in text.split('\n\n'):
        paragraphslist.append(paragraph)
        print(paragraph + '\n' +'-'*50)
    return paragraphslist

def cutsentence(text):
    sentenceslist = list()
    s = SnowNLP(text)
    sentenceslist = s.sentences
    print('\n以下是调用snownlp分句的结果：\n')
    for sentence in sentenceslist:
        print(sentence + '\n' +'-'*50)
    return sentenceslist

def cutword(text):
    wordslist = list()
    sentenceslist = cutsentence(text)
    for sentence in sentenceslist:
        wordslist.extend(jieba.cut(sentence, cut_all=True))
    print('\n以下是调用结巴分词的结果：\n')
    print(wordslist)
    return wordslist

cutparagraph(text)
cutsentence(text)
cutword(text)