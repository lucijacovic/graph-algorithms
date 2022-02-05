# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:50:00 2020

@author: Lucija
"""

import csv

lst=[]

def funk(lst):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            lst.append(line)
    
        result=filter(lambda line: line['K1']=='', lst)

        print("Nisu položili I kolokvij: ")
        #print(list(result))
        popis=[]
        for line in result:
            popis.append(line['mat.'])
        print(popis)

funk(lst)