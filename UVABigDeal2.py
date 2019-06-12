#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:18:41 2019

@author: ep9k
"""
import pandas as pd


#ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#df = pd.DataFrame(ipl_data)
#
#grouped = df.groupby(['Year']).size().tolist()



#
#test_data = {"Name": ['Team1', 'Team2', 'Team1', 'Team2', 'Team3'],
#             "Points": [1, 2, 11, 2, 5]}
#
#df = pd.DataFrame(test_data)
#
#grouped = df.groupby(['Name'])['Points'].sum()
#print(grouped)

#test_data2 = {"Field": ['Physics & Astronomy','Physics & Astronomy','Physics & Astronomy','Physics & Astronomy','Physics & Astronomy', 'Physics & Astronomy', 'Physics & Astronomy', 'Enabling & Strategic Technologies'],
#       "Downloads JR5 2017 in 2017": [0, 151, 90, 89, 737, 42, 28, 97]}
#
#df2 = pd.DataFrame(test_data2)
#grouped2 = df2.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum()
##print(grouped2)

"""This works! Replaces 'N/A' values with 0 and changed formatting of csv column to number"""
data = pd.read_csv('AIP.csv', skiprows=8)
#print(type(data))

sums_by_field = data.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum().tolist()
print(sums_by_field)