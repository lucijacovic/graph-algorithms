# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:51:36 2020

@author: lucijacovic
"""

#from Čović_Lucija_zad1_arcs import susjedi, dat

from Čović_Lucija_zad1_edges import susjedi, dat
matrix={}

def matrica(susjedi, matrix):
    column=susjedi.keys()
    matrix = {k: [1 if x in v else 0 for x in column] for k, v in susjedi.items()}
    return matrix

print("\n")    
print(matrica(susjedi, matrix))
dat.close()