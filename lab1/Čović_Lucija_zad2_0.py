# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:21:42 2020

@author: Lucija
"""

n=int(input("Unesi broj: "))

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

print(prost(n))