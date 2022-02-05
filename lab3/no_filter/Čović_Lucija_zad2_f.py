# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:39:25 2020

@author: Lucija
"""

#zapisuje studente koji su položili ispit u JSON formatu

import csv
import json

lst=[]
json_studenti='{}'

with open('evidencija.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    for line in csv_reader:
        if line['1.rok']!='': #ako nije prazan
            if int(line['1.rok'])>=40:
                lst.append(line['mat.'])
                
        if line['K1']!='' and line['K2']!='' and line['1.rok']=='':
            kolokvij=(int(line['K1']) + int(line['K2']))/2
            if kolokvij>=40:
                lst.append(line['mat.'])        
#print(lst)

def zapisi(json_studenti, lst):
    json_dict=json.loads(json_studenti)
    json_dict['studenti_koji_su_polozili_ispit']=lst
    studenti_json=json.dumps(json_dict) #da vrati JSON file
    return studenti_json

print(zapisi(json_studenti, lst))