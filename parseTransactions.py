#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:19:38 2023

@author: keith
"""
import json
import datetime

f = open('transactions.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
# Closing file
f.close()

json_str = json.dumps(data, indent=4)
 
print(json_str[1:2000])
 
f1 = open("transactions.pretty.json", "w") 
f1.write(json_str)
f1.close() 

cnt = 0
for i in data['items']:
    cnt += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(cnt)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    timeEpochMilli = i['timeEpochMilli']
    txnDateTime = datetime.datetime.fromtimestamp(int(timeEpochMilli)/1000.0)
    print("txnDateTime: {}".format(txnDateTime))
    
    #print(type(i))
    #print(i.keys())
    txn = i['transaction']
    #print(txn.keys())
    txnType = "ADD"
    if 'type' in txn.keys():
       txnType = txn['type']
    print("txnType: {}".format(txnType))
       #print('---- type ----')
       #print(txnType) 
      
    player = txn['player']
    #print('---- player ----')
    #print(player.keys()) 
    playerName = player['proPlayer']['nameFull']
    playerTeam = player['proPlayer']['proTeamAbbreviation']
    playerPosition = player['proPlayer']['position']
    #print(json.dumps(player, indent =2))
    print("Player Name: {}".format(playerName))
    print("playerTeam: {}".format(playerTeam))
    print("position: {}".format(playerPosition))
    team = txn['team']
    #print('---- team ----')
    teamName = team['name'] 
    print("Player Name: {}".format(teamName))
    #print(json.dumps(i,indent=3))
     #print(i)