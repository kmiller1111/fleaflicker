#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:30:51 2023

@author: keith
"""
import os

def processFile(directory, file):
    f = os.path.join(directory, filename)
    print(f)
    
    
directory = 'raw/transactions'
 
for filename in os.listdir(directory):
    processFile(directory, filename)