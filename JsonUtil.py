#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:33:27 2023

@author: keith
"""
import json
    
def savePretty(inFile, prettyFile):
    print("in: {}  out: {}".format(inFile, prettyFile)) 
    f = open(inFile)
    data = json.load(f)
    f.close()

    json_str = json.dumps(data, indent=2)
    f1 = open(prettyFile, "w") 
    f1.write(json_str)
    f1.close() 
    
#savePretty("raw/player/2023-12-13.1.json","silver/playersPretty/2023-12-13.1.json")        