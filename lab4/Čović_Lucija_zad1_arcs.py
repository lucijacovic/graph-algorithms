# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:54:20 2020

@author: lucijacovic
"""

dat=open("football.net", "r")
br=0
susjedi={}

bridovi = []
with open("football.net", "r") as file:
	for line in file:
		if "*Arcs" in line:
			lines = file.readlines()
			for i in lines:
				res = i.split()
				bridovi.append(res)
        
del bridovi[-1]                
#print(bridovi)

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
 	




