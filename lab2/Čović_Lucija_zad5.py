# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:13:44 2020

@author: Lucija
"""

stari={1:[2,3,5], 2:[1, 4], 3:[1,2]}
novi={} #{1:[2,3], 2:[1,3], 3:[1], 4:[2], 5:[1]}

def funk(stari, novi):
    #za stvaranje kljuceva novog rjecnika:
    maxValue = max((max(stari[key]) for key in stari))
    for key in range(1,maxValue+1): #za broj od 1 do 5
        novi[key]=[]
    
    #za stvaranje vrijednosti(lista) novog rjecnika:
    for key_old in stari: #za kljuc u starom
        for key_new in novi: #za kljuc u novom
            for br in stari[key_old]: #za broj u listama starog
                if br==key_new: #ako je element u value starog jednaka key novog
                    novi[key_new].append(key_old) #value novog appenda key starog kao value
    
    novi = dict( [(k,v) for k,v in novi.items() if len(v)>0]) #za brisanje nepotrebnih(praznih) key-eva
    
    return novi

print(funk(stari, novi))