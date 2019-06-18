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
import matplotlib.patches as mpatches
from operator import itemgetter


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
    """Charts references by field for chosen provider. User inputs provider name and dynamically generates chart for that provider.
    References are defined as: 'Number of references made by researchers of your institution to an article from a given journal.' """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
    
    for i in fields_data:
        fields.append(i[0])
        
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['References'].sum().tolist()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'References by UVA authors by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 


def publications_by_field_by_provider(provider_name):
    """Charts publications by field for chosen provider. User inputs provider name and dynamically generates chart for that provider.
    Papers are defined as: 'Number of documents published in peer-reviewed journals indexed in Scopus and for which at least one author was affiliated to your institution.'"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
   
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Papers'].sum().tolist()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Publications by UVA authors by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 

def percent_jr5_of_jr1():
    """Print list of providers, showing ratio of jr5 downloads as % of all downloads(jr1) in 2017"""
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    
    combined = list(zip(jr5_data_by_package, jr1_data_by_package))
    
    final_rank = []
    
    for i in combined:
        provider_name = i[0][0]
        jr5_downloads = i[0][1]
        jr1_downloads = i[0][4]
        final_rank.append((provider_name, round((jr5_downloads/jr1_downloads), 4)))   #round to 4 decimal places
        
    final_rank_sorted = tuple(sorted(final_rank, key=itemgetter(1), reverse=True))
    provider = []
    percent_count = []
    
    for i in final_rank_sorted:
        provider.append(i[0])
        percent_count.append(i[1])
    
#    publishers_list = ['AIP', 'American Chemical Society', 'American Institute of Aeronautics and Astronautics', 'American Mathematical Society', 'American Physical Society', 'American Psychological Association', 
#                       'American Society of Civil Engineers', 'American Society of Mechanical Engineers', 'Annual Reviews', 'Association for Computing Machinery', 'BioOne', 'Brill', 'Cambridge UP', 'DeGruyter', 
#                       'Elsevier', 'Emerald', 'IEEE', 'IOPscience', 'Karger', 'MIT Press', 'Modern Language Association', 'Oxford UP', 'Project MUSE', 'Royal Society of Chemistry', 'Sage', 'SPIE', 'Springer', 
#                       'Taylor & Francis', 'U Chicago Press', 'Wiley']
#    aggregators_list = ['Ebsco', 'Gale', 'ProQuest']
#    hybrids_list = ['Ovid']
#    archives_list = ['JSTOR']
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads')
    plot = plt.barh(provider, percent_count, height=.8, color='green')
    
    plot[29].set_color('red')   #Ebsco, Gale, ProQuest are aggregators
    plot[32].set_color('red')
    plot[33].set_color('red')
    plot[5].set_color('purple')    #Ovid is hybrid
    plot[31].set_color('blue')     #JSTOR is archive
    
    #make custom plot legend
    publishers = mpatches.Patch(color='green', label='Publisher')
    aggregators = mpatches.Patch(color='red', label='Aggregator')
    hybrids = mpatches.Patch(color='purple', label='Hybrid')
    archives = mpatches.Patch(color='blue', label='Archive')
    
    plt.grid()
    plt.legend(handles=[publishers, aggregators, hybrids, archives], title='Provider Type')
    plt.show() 
    

