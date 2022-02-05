# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:54:20 2020

@author: lucijacovic
"""

#za testiranje zadatka 4 (eulerova staza):
#dat=open("euler2.net", "r")

dat=open("euler2.net", "r")
br=0
susjedi={}

def lista_susjedstva(dat,susjedi,br):
    #uzmi vertices kao key
    next(dat)
    for red in dat:
        if (red=="*Arcs\n"):
            break
        else:
            br=br+1
        
    for key in range(1,br+1):
        susjedi[key]=[]
    
    bridovi=[]
    for line in dat:
         if "*Edges\n" in line:
              lines = dat.readlines()
              for i in lines:
                  res = i.split()
                  bridovi.append(res)
         
    del bridovi[-1] #appenda prazni [] na kraju bez ovoga
    #print(bridovi)
    
    for key in susjedi:
        for i in bridovi:
            #i[0] prvi broj, [1] drugi broj
            if int(i[0])==int(key):
                susjedi[key].append(int(i[1]))
            if int(i[1])==int(key):
                susjedi[key].append(int(i[0]))
        susjedi[key].sort()

    return susjedi

print(lista_susjedstva(dat,susjedi,br))
#dat.close()
 	




