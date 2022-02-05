# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:52:59 2020

@author: Lucija
"""

#za danu ocjenu vraća listu studenata koji su dobili tu ocjenu. Rasponi
#za ocjene su po 15 bodova počevši od 40 bodova za ocjenu dovoljan.

# do 39 je 1
# 40 je 2
# 55 je 3
# 70 je 4
# 85 je 5

#kolkvij ocjena: (K1 + K2) / 2

import csv

lst=[]

ocjena=int(input("Unesi ocjenu: "))

def funk(lst, ocjena):
    with open('evidencija.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for line in csv_reader:
            if line['1.rok']!='': #ako nije prazan
                if int(line['1.rok'])<40 and ocjena == 1:
                    lst.append(line['mat.'])
                if int(line['1.rok'])>=40 and int(line['1.rok'])<55 and ocjena == 2:
                    lst.append(line['mat.'])
                if int(line['1.rok'])>=55 and int(line['1.rok'])<70 and ocjena == 3:
                    lst.append(line['mat.'])
                if int(line['1.rok'])>=70 and int(line['1.rok'])<85 and ocjena == 4:
                    lst.append(line['mat.'])
                if int(line['1.rok'])>=85 and ocjena == 5:
                    lst.append(line['mat.'])
                    
            if line['K1']!='' and line['K2']!='' and line['1.rok']=='':
                kolokvij=(int(line['K1']) + int(line['K2']))/2
                if kolokvij<40 and ocjena == 1:
                    lst.append(line['mat.'])
                if kolokvij>=40 and kolokvij<55 and ocjena == 2:
                    lst.append(line['mat.'])
                if kolokvij>=55 and kolokvij<70 and ocjena == 3:
                    lst.append(line['mat.'])
                if kolokvij>=70 and kolokvij<85 and ocjena == 4:
                    lst.append(line['mat.'])
                if kolokvij>=85 and ocjena == 5:
                    lst.append(line['mat.'])
        return lst
        
print(funk(lst, ocjena))
