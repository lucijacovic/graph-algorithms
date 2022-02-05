# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:14:47 2020

@author: Lucija
"""

from random import choice

pobjeda = 0
gubitak = 0
jednako = 0

pravila = {'Kamen': 'Papir', 'Škare': 'Kamen', 'Papir': 'Škare'}
opcije = ['Kamen', 'Papir', 'Škare']

while True:
    igrac=input("Kamen, Škare, Papir ili Kraj? ")
    kompjuter=pravila[choice(opcije)]
    
    if igrac in ("Kraj"):
        print("Pobjedili %d put/a." %pobjeda)
        print("Izgubili %d put/a." %gubitak)
        print("Izjednacenje %d put/a." %jednako)
        break
    
    elif igrac in pravila:
        opcije.append(igrac)
        print("Kompjuter: ", kompjuter, end="")
        
        if pravila[kompjuter]==igrac:
            print("\nPobjedili :)")
            pobjeda+=1
        elif pravila[igrac]==kompjuter:
            print("\nIzgubili :(")
            gubitak+=1
        else:
            print("\nIzjednacenje :/")
            jednako+=1
            
    else:
        print("Krivi unos")
        
    
