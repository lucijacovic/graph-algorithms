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
            if line['K1']=='':
                lst.append(line['mat.'])
        return lst

print("Nisu izašli na I. kolokvij: ", funk(lst))
