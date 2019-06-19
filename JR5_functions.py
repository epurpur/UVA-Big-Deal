#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:12:52 2019

@author: ep9k
"""

"""All functions related to JR5 data"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter


def read_jr5():
    """Make 'Downloads JR5 2017 in 2017' table. JR5 data is all downloads by provider of 2017 articles in 2017"""

    data = pd.read_csv('Packages.csv', skiprows=8)

    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()

    jr5_packages = [x[0] for x in jr5_data_by_package]
    jr5_totals = [x[1] for x in jr5_data_by_package]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017')
    plt.barh(jr5_packages, jr5_totals, height=.8, color='green')
    plt.grid()
    plt.show()


def read_jr5_no_elsevier():
    """Make 'Dowloads JR5 2017 in 2017 table. Remove 'Elsevier' from results
    so table looks better. JR5 data is all downloads by provider of 2017 articles in 2017"""

    data = pd.read_csv('Packages.csv', skiprows=8)

    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    
    for i in jr5_data_by_package:
        if i[0] == 'Elsevier':
            jr5_data_by_package.remove(i)

    jr5_packages = [x[0] for x in jr5_data_by_package]
    jr5_totals = [x[1] for x in jr5_data_by_package]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017 (without Elsevier)')
    plt.barh(jr5_packages, jr5_totals, height=.8, color='green')
    plt.grid()
    plt.show()


def jr5_big5():
    """Showing jr5 data for big 5 providers only
    Big 5 are: Elsevier, Wiley, Springer, Taylor & Francis, Sage"""
    
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    jr5_data = []

    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    for i in jr5_data_by_package:
        if i[0] in big5:
            jr5_data.append(i)
    
    big5_packages = [x[0] for x in jr5_data]
    big5_totals = [x[1] for x in jr5_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017 (Big5 Providers)')
    plt.barh(big5_packages, big5_totals, height=.8, color='green')
    plt.grid()
    plt.show()
    
    
def jr5_other_providers():
    """Showing jr5 data for all other providers outside big 5"""
    
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    jr5_data = []
    
    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    for i in jr5_data_by_package:
        if i[0] not in big5:
            jr5_data.append(i)
  
    jr5_packages = [x[0] for x in jr5_data_by_package]
    jr5_totals = [x[1] for x in jr5_data_by_package]
    
    jr5_packages = [x[0] for x in jr5_data]
    jr5_totals = [x[1] for x in jr5_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017 (Not Big5 Providers)')
    plt.barh(jr5_packages, jr5_totals, height=.8, color='green')
    plt.grid()
    plt.show()    
        
        
def jr5_by_field_by_provider(provider_name):
    """Charts JR5 downloads by field for chosen provider. User inputs provider name and dynamically generates chart for that provider"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR5 Downloads by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 
    
    
def jr5_percent_field_by_provider(provider_name):
    """Charts % of JR5 downloads by field for a given provider. This is in lieu of a stacked bar graph"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])

    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer

    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum().tolist()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    total_downloads = sum(sums_by_field)
        
    percent_by_field = [round((i/total_downloads), 4) for i in sums_by_field]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent of total JR5 downloads by field for: {provider_name}')
    plt.barh(fields, percent_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 

    
def jr5_fluff_checker(provider_name):
    """Checking for fluff in different providers. The hypothesis is that most packages provide a small number of 
    highly used journals and the rest are fluff that we are paying for. We will look at individual titles per package
    and see which of those make up 80% of the JR5 downloads"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)   
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
    for i in journals_data:
        if i[0] == provider_name:
            journals_data.remove(i)                 #removing aggregator column data
        
    total_jr5_downloads = 0
    total_journals = 0                         
    for i in journals_data:
        total_jr5_downloads += i[3]
        total_journals += 1
        
    jr5_tuples = [(i[0], i[3]) for i in journals_data]
    jr5_tuples_sorted = sorted(jr5_tuples, key = lambda x: x[1], reverse=True)       #sorts on second element of jr5_tuples
        
    running_tally = 0
    highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
    for i in jr5_tuples_sorted:
        if running_tally < (total_jr5_downloads * 0.8):
            highly_used_journals.append(i)
            running_tally += i[1]
#            print("Adding:", i[1])
#            print("Total:", running_tally)
            
#    print(highly_used_journals)
    print(f"Total JR5 downloads for provider: {provider_name} = {total_jr5_downloads}")
    print(f"{len(highly_used_journals)} of {total_journals} journals make up 80% of the use")
    
    fluff_index = ((len(highly_used_journals))/(total_journals))
    print(f"Fluff index = {fluff_index}")
    
    if fluff_index < .20:
        print("Seems fluffy to me!")
    

def jr5_fluff_index():
    """Produces 'fluff index' value by provider for JR5 downloads and charts each provider and its corresponding fluff index.
    Fluff index is basically a ratio of highly used journals to total journals for each provider. We are checking to see if providers
    are including a bunch of unused journals in their offerings.
    Here is how fluff index is calculated:
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates fluff score as number of journals required to reach 80% / total journals by provider
        - Charts fluff index of all providers, with Big 5 in red"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
    
    providers = [i[0] for i in providers]
        
    fluff_by_provider = []
    
    for provider_name in providers:
        subset_by_provider = data.loc[data['Provider'] == provider_name]
      
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr5_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr5_downloads += i[3]
            total_journals += 1

        jr5_tuples = [(i[0], i[3]) for i in journals_data]
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr5_tuples_sorted:
            if running_tally < (total_jr5_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
    
        fluff_index = ((len(highly_used_journals))/(total_journals))
            
        fluff_by_provider.append((provider_name, fluff_index))
        
    fluff_by_provider = sorted(fluff_by_provider, key=itemgetter(1), reverse=True)    #sorting by fluff_index score
    
    providers = [x[0] for x in fluff_by_provider]
    fluff_score = [x[1] for x in fluff_by_provider]
    
    #plot results
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR5 Fluff Index by provider')
    plot = plt.barh(providers, fluff_score, height=.8, color='green')
    
    plot[15].set_color('red')
    plot[19].set_color('red')
    plot[20].set_color('red')
    plot[21].set_color('red')
    plot[25].set_color('red')
    
    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show() 
        

jr5_fluff_index()




