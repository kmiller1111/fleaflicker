#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:33:15 2023

@author: keith
"""
import json
import datetime


def parse(inFile, outFileName):
    print("in: {}  out: {}".format(inFile, outFileName)) 
    f = open(inFile)
    data = json.load(f)
    # Closing file
    f.close()
    outFile = open(outFileName, 'w')
    
    cnt = 0
    for i in data['items']:
        cnt += 1
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #print(cnt)
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        timeEpochMilli = i['timeEpochMilli']
        txnDateTime = datetime.datetime.fromtimestamp(int(timeEpochMilli)/1000.0)
        #print("txnDateTime: {}".format(txnDateTime))
        
        #print(type(i))
        #print(i.keys())
        txn = i['transaction']
        #print(txn.keys())
        txnType = "ADD"
        if 'type' in txn.keys():
           txnType = txn['type'].replace("TRANSACTION_","")
        #print("txnType: {}".format(txnType))
           #print('---- type ----')
           #print(txnType) 
          
        player = txn['player']
        #print('---- player ----')
        #print(player.keys()) 
        playerName = player['proPlayer']['nameFull']
        playerTeam = player['proPlayer']['proTeamAbbreviation']
        playerPosition = player['proPlayer']['position']
        #print(json.dumps(player, indent =2))
        #print("Player Name: {}".format(playerName))
        #print("playerTeam: {}".format(playerTeam))
        #print("position: {}".format(playerPosition))
        team = txn['team']
        #print('---- team ----')
        teamName = team['name'] 
        #print("Team Name: {}".format(teamName))
        #print(json.dumps(i,indent=3))
         #print(i)
        outLine = "{},{},{},{},{},{}".format(txnDateTime,teamName,txnType,playerName,playerTeam,playerPosition)
        print(outLine)
        outFile.write(outLine + "\n")
        
    outFile.close() 