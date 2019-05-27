#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:23:49 2019

@author: mw404851
"""
from os import (
           listdir,
           path,
           makedirs
)

class Dir():
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.files = listdir(sciezka)
        
    def __repr__(self):
        
        return '(Dir' + self.sciezka +")"
    def __dir__(self):
        return self.files
    
    def __getattr__(self, string):
        if string in self.files:
            x = path.join(self.sciezka, string)
            if path.isdir(x):
                return Dir(x)
            else:
                with open(x) as f: 
                    return f.read()
        else:
            raise AttributeError("Blad w stringu") 
            
d = Dir(".") 
print(d.drzewo)
print(d.tresc)
