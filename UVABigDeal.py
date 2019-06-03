#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:25:09 2019

@author: ep9k
"""

"""Source file here to show how we've been interpreting the 1figr data. Data
about UVA's big deal scholarly publication contracts"""

import pandas as pd
import numpy as np

data = pd.read_csv("JournalsPerProvider.csv", skiprows=8)                   #8 unnecessary rows before we get to column headers

#print(list(data.columns.values))                #list of column headers
#print(data['Provider'])                             #can call column headers like this

provider_names = []
for row in data['Provider']:
    if row not in provider_names:
        provider_names.append(row)
        
print(provider_names)                           #prints list of provider names (36 in total)
    


