#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:18:41 2019

@author: ep9k
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("JournalsPerProvider.csv", skiprows=8)


#result1 = data[data['Provider'] == 'AIP'].groupby('Field', as_index=False).sum().values.tolist()
#print(result1)

data = pd.read_csv('Packages.csv', skiprows=8)


import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.2
 
# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
print(r2)
print(r3)

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
 
# Create legend & Show graphic
#plt.legend()
#plt.show()
