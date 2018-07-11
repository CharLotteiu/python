# -*- coding: utf-8 -*-
"""
@author: Charlotte
"""


import re, os
from stanfordcorenlp import StanfordCoreNLP
import matplotlib.pyplot as plt 

class WordFreq:
    def __init__(self):
        self.text_cn=[]
        self.text_en=[]
        self.tag_cn=[]
        self.tag_en=[]
        self.en={}
        self.cn={}
    
    def duquwenjian(self,files):
        for file in files:
            filepath = file
            for eachLine in open(filepath,'r',encoding='UTF-8'):
                p1 = re.compile(r'[^(A-Za-z)+$]')
                p2 = re.compile(r'[^\u4e00-\u9fa5]')                    #中文的编码范围是：\u4e00到\u9fa5		
                zh = " ".join(p2.split(eachLine)).strip()                    
                zh = ",".join(zh.split())
                en = " ".join(p1.split(eachLine)).strip()                    
                en = ",".join(en.split())
                self.text_cn.append(zh)
                self.text_en.append(en)

    
    def cixinbiaozhu(self):
        nlp_en = StanfordCoreNLP(r'D:/Applications/python 3.6.5/stanford-corenlp-full-2018-02-27', lang='en')
        nlp_cn = StanfordCoreNLP(r'D:/Applications/python 3.6.5/stanford-corenlp-full-2018-02-27', lang='zh')
        all_text_cn = ""
        all_text_en = ""
        for line in self.text_cn:
            all_text_cn += line
        for line in self.text_en:
            all_text_en += line
        self.tag_cn = nlp_cn.pos_tag(all_text_cn)
        self.tag_en = nlp_en.pos_tag(all_text_en)
    
    def tongjicixin(self):
        for index, unit in enumerate(self.tag_cn):
            cixin = self.tag_cn[index][1]
            if cixin not in self.cn:
                self.cn[cixin] = 0
            self.cn[cixin] += 1
        for index, unit in enumerate(self.tag_en):
            cixin = self.tag_en[index][1]
            if cixin not in self.en:
                self.en[cixin] = 0
            self.en[cixin] += 1
    
    def showplot(self):
        ensort = sorted(self.en.items(),key = lambda item:item[1],reverse=True)
        cnsort = sorted(self.cn.items(),key = lambda item:item[1],reverse=True)
        
        cixintop5L_en = []
        cixintop5V_en = []
        cixintop5L_cn = []
        cixintop5V_cn = []
        for i in range(5):
            cixintop5L_en.append(ensort[i][0])
            cixintop5V_en.append(ensort[i][1])
            cixintop5L_cn.append(cnsort[i][0])
            cixintop5V_cn.append(cnsort[i][1])
        
        cixinother_en = ensort[5:]
        cixinother_cn = cnsort[5:]
        cixinotherV_en=[]
        cixinotherL_en=['Others']
        cixinotherV_cn=[]
        cixinotherL_cn=['其他词性']
        for unit in cixinother_en:
            cixinotherV_en.append(unit[1])
        for unit in cixinother_cn:
            cixinotherV_cn.append(unit[1])
        
        labels_en = cixintop5L_en + cixinotherL_en
        labels_cn = cixintop5L_cn + cixinotherL_cn
        X_en = cixintop5V_en
        X_en.append(sum(cixinotherV_en))
        X_cn = cixintop5V_cn
        X_cn.append(sum(cixinotherV_cn))
        
        plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
        plt.figure(figsize=(9,9))
        plt.pie(X_en,labels=labels_en,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
        plt.title("英文词性分布图")
        plt.show()
        
        plt.figure(figsize=(6,9))
        plt.pie(X_cn,labels=labels_cn,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
        plt.title("中文词性分布图")
        plt.show()
    
    def run(self,files):
        self.duquwenjian(files)
        self.cixinbiaozhu()
        self.tongjicixin()
        self.showplot()
        
wf = WordFreq()
files=[]
filedir = os.getcwd()+'/bilingual'
filenames=os.listdir(filedir)
for filename in filenames:
    file = filedir + '/' + filename
    files.append(file)
    
wf.run(files)


