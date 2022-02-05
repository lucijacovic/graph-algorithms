# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:17:14 2020

@author: lucijacovic
"""

#from Čović_Lucija_zad1_arcs import susjedi, dat

from Čović_Lucija_zad1_edges import susjedi, dat
import random

#datoteka iz prvog zadatka je euler.net koja nije Eulerov graf!
#prvo treba u zad1 promjeniti da čita datoteku "euler2.net" koja je Eulerov graf
#i tek onda pokreniti ovaj kod

stupnjevi={}
susjedi_k=[]
staza=[]

def eulerov_graf(dat,susjedi,stupnjevi,susjedi_k,staza):
    for key in susjedi:
        stupnjevi[key]=[]
        susjedi_k.append(key)
   
    for k in stupnjevi:
        for key in susjedi:
            if k==key:
                stupnjevi[k].append(len(susjedi[key]))
    
    print("Keys:\n", susjedi_k)
    print("Lista susjedstva:\n", susjedi)
    print("Stupnjevi vrhova:\n", stupnjevi)
    
    #provjera je li Eulerov graf
    for key in stupnjevi:
        for digit in stupnjevi[key]:
            if digit % 2 == 0: 
                continue
            else:
                return False #("Nije Eulerov graf.")
                break
        return True #("Eulerov graf!")

print("Eulerov graf?\n", eulerov_graf(dat,susjedi,stupnjevi,susjedi_k,staza))

#sve sam probala, ali nikako ne mogu napraviti da mi se
#funkcija eulerova_staza izvrši samo ako eulerov_graf vraća True

def eulerova_staza(staza, susjedi, susjedi_k):
    # if not eulerov_graf(dat,susjedi,stupnjevi,susjedi_k,staza):
    #     return []
    a=random.choice(susjedi_k)
    staza.append(a)
    while len(susjedi_k)>0:   
        for key in susjedi:
            if a in susjedi_k:
                susjedi_k.remove(a)
            if a==key: #ako je prvi jedan keyu, staza appenda random br iz list od key-a
                b=random.choice(susjedi[key])
                staza.append(b)
                susjedi[key].remove(b)
                if b in susjedi_k:
                    susjedi_k.remove(b)

    return staza

print("Eulerova staza:\n", eulerova_staza(staza, susjedi, susjedi_k))
dat.close()