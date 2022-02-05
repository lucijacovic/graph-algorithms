# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:09:46 2020

@author: lucijacovic
"""

# import csv
import pandas as pd
# from itertools import permutations
# perms = list(permutations(range(n), n))

distance=pd.read_csv("distance.csv", index_col=0, squeeze=True).to_dict()

# city_number=0

# for i in distance:
#     city_number=city_number+1

#prominit udaljenost iz stringa u integer, maknit prazne podatke npr. 'Zurich': '-'    
for key, value in list(distance.items()):
    for k, v in list(value.items()):
        if v=='-':
            value.pop(k) #radi?
        else:
            v==int(v) #ne radi

print(distance)
#print(city_number)
print(len(distance.keys())) #broj gradova
print(distance.keys())