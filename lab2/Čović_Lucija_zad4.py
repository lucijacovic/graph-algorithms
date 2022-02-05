# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:29:48 2020

@author: Lucija
"""

#rijeci.txt = ana mama ana banana ana ana banana
#ana 4, mama 1, banana 2

from collections import defaultdict

dat=open("rijeci.txt", "r")

def ponavljanje(dat):
    rjecnik=defaultdict(int)
    for red in dat:
        for rijec in red.split():
            rjecnik[rijec]+=1
    print(rjecnik)

ponavljanje(dat)
dat.close()

    

    