#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:04:23 2019

@author: mw404851
"""

class Chain:
    def __init__(self):
        self.com = []
    def append(self, comp):
        self.com.append(comp)
    def __call__(self, x):
        for f in self.com:
            if not hasattr(f,"warunek"):
                x = f(x)
                print(x)
        return x
                
                
    def __setitem__(self, item, value):
        self.com[item] = value
            
    def __getitem__(self, item):
        return self.com[item]
            

    
c = Chain()
c.append(lambda x: x+2) # append
c.append(lambda y: y*2)


print(c(1))   # (1 + 2 ) * 2 = 6     __call__

c[0] = lambda x: x+3    # __setitem__

c[1].warunek = lambda y:y>0  # precondition dla funkcji 1

print(c(-2))  # -2 + 3 = 1 > 0, wiÄ™c liczymy dalej 1 * 2 = 2 
print(c(-4))  # -4 + 3 = -1 <= 0, wiÄ™c dalej nie liczymy