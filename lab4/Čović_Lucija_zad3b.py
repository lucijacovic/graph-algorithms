# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:00:20 2020

@author: lucijacovic
"""

#from Čović_Lucija_zad1_arcs import dat, susjedi

from Čović_Lucija_zad1_edges import dat, susjedi
br=0

def broj_bridova(dat,br, susjedi):
    for key in susjedi:
        for lst in susjedi[key]:
            br=br+1
            
    return int(br/2)

print("\nBroj bridova:", broj_bridova(dat,br, susjedi))
dat.close()