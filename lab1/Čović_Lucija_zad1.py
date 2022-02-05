# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:21:17 2020

@author: Lucija
"""

n=int(input("Unesi broj redova: "))

def trokut(n):
    for i in range(n):
        k=i+1
        for j in range(i+1):
            if(k<10):
                print(" ",k,end="")
            else:
                print(" ",k%10,end="")
            k=k+1
        k=k-2
        for j in range(i,0,-1):
            if(k<10):
                print(" ",k,end="")
            else:
                print(" ",k%10,end="")
            k=k-1
        print()
        
trokut(n)