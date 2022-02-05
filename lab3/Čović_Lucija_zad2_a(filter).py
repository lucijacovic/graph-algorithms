# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:45:50 2020

@author: Lucija
"""

#vraća prosječni rezultat na kolokvijima, odnosno na prvom ispitnom roku

import csv

lst1=[]
lst2=[]
lst3=[]

def funk(lst1,lst2,lst3):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            lst1.append(line)
            lst2.append(line)
            lst3.append(line)
            
        result1=filter(lambda line: line['K1']!='', lst1)
        result2=filter(lambda line: line['K2']!='', lst2)
        result3=filter(lambda line: line['1.rok']!='', lst3)
        
        k1_ocjene=0
        k2_ocjene=0
        ispit_ocjene=0
        k1_br=0
        k2_br=0
        ispit_br=0           
        
        for line in result1:
             k1_br=k1_br+1
             k1_ocjene=int(line['K1'])+k1_ocjene
            
        for line in result2:
            k2_br=k2_br+1
            k2_ocjene=int(line['K2'])+k2_ocjene
        
        for line in result3:
            ispit_br=ispit_br+1
            ispit_ocjene=int(line['1.rok'])+ispit_ocjene
    
        print("Prosječni rezultat na prvom kolokviju je:", k1_ocjene/k1_br)
        print("Prosječni rezultat na drugom kolokviju je:", k2_ocjene/k2_br)
        print("Prosječni rezultat na ispitu je:", ispit_ocjene/ispit_br)

funk(lst1,lst2,lst3)