# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:44:20 2020

@author: lucijacovic
"""

#from Čović_Lucija_zad1_arcs import dat, susjedi

from Čović_Lucija_zad1_edges import dat, susjedi
br=0

def broj_vrhova(dat,br, susjedi):
    for key in susjedi:
        br=br+1
        
    return br

print("\nBroj vrhova:", broj_vrhova(dat,br, susjedi))
dat.close()
