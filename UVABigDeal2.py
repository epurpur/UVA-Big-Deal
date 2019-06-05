#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:18:41 2019

@author: ep9k
"""

import pandas as pd

data = pd.read_csv("JournalsPerProviderTest.csv")


result1 = data[data['Provider'] == 'AIP'].groupby('Field', as_index=False).sum().values.tolist()
print(result1)