# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:36:27 2020

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

#iznimka: 1 nije prosti broj tako da se 2 (parni broj) ne može napisati kao zbroj prostih brojeva

parni=int(input("Unesi parni broj: "))

def zbroj(parni):
    if(parni%2!=0) or parni==2:
        print("Uneseni broj nije parni / Uneseni broj je 2")
        return
    for i in range(2,parni+1):
        for j in range(2,i+1):
            if (prost(i))==True and (prost(j))==True and i+j==parni:
                if(i==j):
                    print(i,"+",j)
                else:
                    print(i,"+",j)
                    print(j,"+",i)

zbroj(parni)