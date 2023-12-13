#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:30:51 2023

@author: keith
"""
import os
import transactionParser as tp

indir = 'raw/transactions'
outdir = 'silver/transactions'


def processFile(directory, file):
    inFile = os.path.join(directory, filename)
    outFile = os.path.join(outdir, filename)
    tp.parse(inFile, outFile)    
    
    
 
for filename in os.listdir(indir):
    processFile(indir, filename)