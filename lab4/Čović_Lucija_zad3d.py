# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:58:39 2020

@author: lucijacovic
"""

#from Čović_Lucija_zad1_arcs import susjedi, dat

from Čović_Lucija_zad1_edges import susjedi, dat
stupnjevi={}

def vrhovi_max(dat,susjedi,stupnjevi):
    for key in susjedi:
        stupnjevi[key]=[]
   
    for k in stupnjevi:
        for key in susjedi:
            if k==key:
                stupnjevi[k].append(len(susjedi[key]))
    
    vrhovi=[k for k, v in stupnjevi.items() if v == max(stupnjevi.values())]
    return vrhovi

print("\nVrhovi s maksimalnim brojem incidentnih bridova su: ", vrhovi_max(dat,susjedi,stupnjevi))
dat.close()
