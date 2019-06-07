#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:18:41 2019

@author: ep9k
"""

import pandas as pd

data = pd.read_csv("JournalsPerProvider.csv", skiprows=8)


#result1 = data[data['Provider'] == 'AIP'].groupby('Field', as_index=False).sum().values.tolist()
#print(result1)

data = pd.read_csv('Packages.csv', skiprows=8)


#print("Unique Domains:", data.Domain.unique())
#print()
#print("Unique Fields:", data.Field.unique())

#
#fields_data = data.groupby(['Field', 'Downloads JR5 2017 in 2017'])
#for i in fields_data:
#    print(i)


packages = ['AIP', 'American Chemical Society', 'American Institute of Aeronautics and Astronautics', 'American Mathematical Society', 'American Physical Society', 'American Psychological Association', 'American Society of Civil Engineers', 'American Society of Mechanical Engineers', 'Annual Reviews', 'Association for Computing Machinery', 'BioOne', 'Brill', 'Cambridge UP', 'DeGruyter', 'Ebsco', 'Elsevier', 'Emerald', 'Gale', 'IEEE', 'IOPscience', 'JSTOR', 'Karger', 'MIT Press', 'Modern Language Association', 'Ovid', 'Oxford UP', 'ProQuest', 'Project MUSE', 'Royal Society of Chemistry', 'SPIE', 'Sage', 'Springer', 'Taylor & Francis', 'U Chicago Press', 'Wiley']

unwanted = ['Elsevier', 'Wiley', 'Sage', 'Taylor & Francis', 'Springer']
big5 = []

for i in packages:
    if i in unwanted:
        packages.remove(i)
        big5.append(i)

for i in packages:
    print(i)
    
print()
for i in big5:
    print(i)