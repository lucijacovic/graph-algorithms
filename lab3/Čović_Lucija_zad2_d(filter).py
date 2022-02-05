# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:30:26 2020

@author: Lucija
"""

#vraća prosječni rezultat onih studenata koji su položili ispit

import csv

lst=[]

def funk(lst):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            lst.append(line)
        
        result=filter(lambda line: line['1.rok']!='' and int(line['1.rok'])>=40, lst)
        
        ocjene=0
        br=0
        for line in result:
            br=br+1
            ocjene=int(line['1.rok'])+ocjene
        
        return ocjene/br
    
print("Prosječni rezultat na ispitu je: ", funk(lst))