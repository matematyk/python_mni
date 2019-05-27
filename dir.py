#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:23:49 2019

@author: mw404851
"""
from os import (
           listdir,
           join,
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
            if isdir(join(self.sciezka, string)):
                makedirs(path)
        try: 
            return "string"
        except:
            raise AttributeError("Blad w stringu") 