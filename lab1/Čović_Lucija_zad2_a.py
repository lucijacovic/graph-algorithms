# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:08:28 2020

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

d1=float(input("Unesi prvi decimalni broj: "))
d2=float(input("Unesi drugi decimalni broj: "))

#bez sljedeće dvije linije pokazuje: TypeError: 'float' object cannot be interpreted as an integer
#pokušala sam i s import numpy & from numpy import arange, ništa ne funkcionira :(
d1=int(d1)
d2=int(d2)

def koliko(d1,d2):
    br=0
    for num in range(d1+1, d2+1):
        if prost(num)==False:
            continue
        else:
            br=br+1
    return br
         
print("Broj prostih brojeva: ", koliko(d1,d2))