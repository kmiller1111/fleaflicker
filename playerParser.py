#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:15:17 2023

@author: keith
"""

import json
import datetime


def parse(inFile):
    print(inFile)
    f = open(inFile)
    data = json.load(f)
    f.close()

    json_str = json.dumps(data, indent=2)
    f1 = open("players.pretty.json", "w") 
    f1.write(json_str)
    f1.close() 
    
parse("raw/player/2023-12-12.json")    