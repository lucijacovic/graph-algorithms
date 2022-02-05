# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:45:50 2020

@author: Lucija
"""

#vraća prosječni rezultat na kolokvijima, odnosno na prvom ispitnom roku

import csv

k1_ocjene=0
k2_ocjene=0
ispit_ocjene=0
k1_br=0
k2_br=0
ispit_br=0

def funk(k1_ocjene, k2_ocjene, ispit_ocjene, k1_br, k2_br, ispit_br):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            if line['K1']!='': #ako nije prazan
                k1_br=k1_br+1    #zbrajaj studenta
                k1_ocjene=int(line['K1'])+k1_ocjene   
                
            if line['K2']!='': #ako nije prazan
                k2_br=k2_br+1    #zbrajaj studenta
                k2_ocjene=int(line['K2'])+k2_ocjene
                
            if line['1.rok']!='': #ako nije prazan
                ispit_br=ispit_br+1    #zbrajaj studenta
                ispit_ocjene=int(line['1.rok'])+ispit_ocjene
    
        print("Prosječni rezultat na prvom kolokviju je:", k1_ocjene/k1_br)
        print("Prosječni rezultat na drugom kolokviju je:", k2_ocjene/k2_br)
        print("Prosječni rezultat na ispitu je:", ispit_ocjene/ispit_br)

funk(k1_ocjene, k2_ocjene, ispit_ocjene, k1_br, k2_br, ispit_br)