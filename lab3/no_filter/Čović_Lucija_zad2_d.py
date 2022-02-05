# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:30:26 2020

@author: Lucija
"""

#vraća prosječni rezultat onih studenata koji su položili ispit

import csv

ocjene=0
br=0

def funk(ocjene, br):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            if line['1.rok']!='' and int(line['1.rok'])>=40: #ako nije prazan i prošli ispit
                br=br+1    #zbrajaj studenta
                ocjene=int(line['1.rok'])+ocjene
                
        return ocjene/br
    
print("Prosječni rezultat na ispitu je: ", funk(ocjene, br))