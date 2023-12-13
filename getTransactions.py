#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:48:50 2023

@author: keith
"""

import requests

params = {
    'sport': 'NHL',
    'league_id': '15754',
}

response = requests.get('https://www.fleaflicker.com/api/FetchLeagueTransactions', params=params)