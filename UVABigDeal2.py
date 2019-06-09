#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:18:41 2019

@author: ep9k
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


data = pd.read_csv("JournalsPerProvider.csv", skiprows=8)


#result1 = data[data['Provider'] == 'AIP'].groupby('Field', as_index=False).sum().values.tolist()
#print(result1)

my_tuple = (
    ('A','Apple'),
    ('C','Carrot'),
    ('B','Banana'),
)

print(my_tuple)

my_tuple_sorted = tuple(sorted(my_tuple, key=itemgetter(1)))

print(my_tuple_sorted)


