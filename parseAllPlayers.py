#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:30:51 2023

@author: keith
"""
import os
#import transactionParser as tp
import JsonUtil 

indir = 'raw/player'
prettyDir = 'silver/playersPretty'
outdir = 'silver/playerss'


def processFile(directory, file):
    inFile = os.path.join(directory, filename)
    #outFile = os.path.join(outdir, filename)
    prettyFile = os.path.join(prettyDir, filename)
    #tp.parse(inFile, outFile)
    JsonUtil.savePretty(inFile, prettyFile)    
    
    
 
for filename in os.listdir(indir):
    processFile(indir, filename)