# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:23:33 2020

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

broj=int(input("Unesi broj: "))

def susjedni(broj):
    for i in range(2,broj+1):
        if(prost(i))==True and (prost(i+2))==True:
            print(i,",",i+2)

susjedni(broj)