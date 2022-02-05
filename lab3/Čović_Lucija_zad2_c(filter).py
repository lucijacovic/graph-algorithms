# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:21:29 2020

@author: Lucija
"""

import csv

lst=[]

def funk(lst):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            lst.append(line)

        result=filter(lambda line: line['K1']=='' and line['K2']=='' and line['1.rok']=='', lst)
        
        br=0
        for line in result:
            br=br+1
        return br

print(funk(lst), "studenata nije izašlo ni na jedan ispit/kolokvij.")
