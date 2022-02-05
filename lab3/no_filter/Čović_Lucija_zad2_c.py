# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:21:29 2020

@author: Lucija
"""

import csv

br=0

def funk(br):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            if line['K1']=='' and line['K2']=='' and line['1.rok']=='':
                br=br+1
        return br

print(funk(br), "studenata nije izašlo ni na jedan ispit/kolokvij.")
