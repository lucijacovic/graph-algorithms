# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:16:49 2020

@author: Lucija
"""

recenica="Ovo je jedna recenica"

def okreni(recenica):
    rijeci=recenica.split(' ')
    obrnuta=' '.join(reversed(rijeci))
    return obrnuta

print(okreni(recenica))