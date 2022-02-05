# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:24:33 2020

@author: Lucija
"""

#n=int(input("Unesi broj: "))

def prost(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

#print(prost(n))

broj=1000000  #ne znam kako definirati beskonačni broj...
fak=int(input("Unesi koji prosti faktor želiš: "))

def vrati(broj,fak):
    br=0
    for i in range(2,broj+1):
        if(prost(i))==True:
            br=br+1
            if(br==fak):
                return i
            
print(vrati(broj,fak))