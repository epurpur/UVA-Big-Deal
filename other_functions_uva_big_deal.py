#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:12:53 2019

@author: ep9k
"""

"""All functions not specifically associated with jr1 or jr5 data"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



def journals_by_domain():
    """Counting occurrences of downloads in each domain from JournalsPerPackage.csv"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    domains_list = data.Domain.tolist()

    counted_domains = pd.Series(domains_list).value_counts().reset_index().values.tolist()
    
    domains = [x[0] for x in counted_domains]
    counts = [x[1] for x in counted_domains]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Journals by Domain')
    plt.barh(domains, counts, height=.8, color='green')
    plt.grid()
    plt.show()
    
    
def journals_by_field():
    """Counting occurrences of downloads in each field from JournalsPerPackage.csv"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    fields_list = data.Field.tolist()

    counted_fields = pd.Series(fields_list).value_counts().reset_index().values.tolist()
    
    fields = [x[0] for x in counted_fields]
    counts = [x[1] for x in counted_fields]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Journals by field')
    plt.barh(fields, counts, height=.8, color='green')
    plt.grid()
    plt.show() 


def journals_by_field_big5():
    """Counting occurences of downloads in each field from Journals Per Package.csv
    from the big5 publishers. Big 5 are: Elsevier, Wiley, Springer, Sage, Taylor & Francis"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    providers_list = data.Provider.tolist()
    fields_list = data.Field.tolist()
    
    zipped = list(zip(providers_list, fields_list))
    
    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    big5_data = []
    
    for i in zipped:
        if i[0] in big5:
            big5_data.append(i)
            
    fields_only = [x[1] for x in big5_data]
    
    counted_fields = pd.Series(fields_only).value_counts().reset_index().values.tolist()
    
    fields = [x[0] for x in counted_fields]
    counts = [x[1] for x in counted_fields]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Journals by field (Big5 Providers)')
    plt.barh(fields, counts, height=.8, color='green')
    plt.grid()
    plt.show() 
    
def journals_by_field_other_providers():
    """Counting occurences of downloads in each field from Journals Per Package.csv
    from the big5 publishers. Big 5 are: Elsevier, Wiley, Springer, Sage, Taylor & Francis"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    providers_list = data.Provider.tolist()
    fields_list = data.Field.tolist()
    
    zipped = list(zip(providers_list, fields_list))
    
    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    not_big5_data = []
    
    for i in zipped:
        if i[0] not in big5:
            not_big5_data.append(i)
            
    fields_only = [x[1] for x in not_big5_data]
    
    counted_fields = pd.Series(fields_only).value_counts().reset_index().values.tolist()
    
    fields = [x[0] for x in counted_fields]
    counts = [x[1] for x in counted_fields]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Journals by Field (Not Big5 Providers)')
    plt.barh(fields, counts, height=.8, color='green')
    plt.grid()
    plt.show() 


def references_by_field_by_provider(provider_name):
    """Charts references by field for chosen provider. User inputs provider name and dynamically generates chart for that provider"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    sums_by_field = subset_by_provider.groupby(['Field'])['References'].sum()     #sum of downloads per field
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'References by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 


def publications_by_field_by_provider(provider_name):
    """Charts publications by field for chosen provider. User inputs provider name and dynamically generates chart for that provider"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Papers'].sum()     #sum of downloads per field
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Publications by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 

  
