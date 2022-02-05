# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:03:49 2020

@author: Lucija
"""

lst1={1,2,3,4}
lst2=set([4,5,6,1])


def presjek(lst1,lst2):
    p=lst1.intersection(lst2)
    return p

print(presjek(lst1,lst2))
    

    