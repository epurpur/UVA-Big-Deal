#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:12:51 2019

@author: ep9k
"""

"""All functions related to JR1 data"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np

def read_jr1():
    """Make downloads 'JR1 2017' table. JR1 data is all downloads per provider for all years"""
    
    data = pd.read_csv('Packages.csv', skiprows=8)

    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    jr1_packages = [x[0] for x in jr1_data_by_package]
    jr1_totals = [x[1] for x in jr1_data_by_package]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR1 2017')
    plt.barh(jr1_packages, jr1_totals, height=.8, color='green')
    plt.grid()
    plt.show()


def read_jr1_no_elsevier():
    """Make downloads 'JR1 2017' table. Remove 'Elsevier' from results to make table nicer to look at. 
    JR1 data is all downloads per provider for all years"""

    data = pd.read_csv('Packages.csv', skiprows=8)

    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    for i in jr1_data_by_package:
        if i[0] == 'Elsevier':
            jr1_data_by_package.remove(i)

    jr1_packages = [x[0] for x in jr1_data_by_package]
    jr1_totals = [x[1] for x in jr1_data_by_package]
       
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR1 2017 (without Elsevier)')
    plt.barh(jr1_packages, jr1_totals, height=.8, color='green')
    plt.grid()
    plt.show()


def jr1_big5():
    """Showing jr1 data for big 5 providers only
    Big 5 are: Elsevier, Wiley, Springer, Taylor & Francis, Sage"""
    
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    jr1_data = []

    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    for i in jr1_data_by_package:
        if i[0] in big5:
            jr1_data.append(i)
    
    big5_packages = [x[0] for x in jr1_data]
    big5_totals = [x[1] for x in jr1_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR1 in 2017 (Big5 Providers)')
    plt.barh(big5_packages, big5_totals, height=.8, color='green')
    plt.grid()
    plt.show()


def jr1_other_providers():
    """Showing jr1 data for all other providers outside big 5"""
    
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    jr1_data = []
    
    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    for i in jr1_data_by_package:
        if i[0] not in big5:
            jr1_data.append(i)
  
    jr1_packages = [x[0] for x in jr1_data_by_package]
    jr1_totals = [x[1] for x in jr1_data_by_package]
    
    jr1_packages = [x[0] for x in jr1_data]
    jr1_totals = [x[1] for x in jr1_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR1 in 2017 (Not Big5 Providers)')
    plt.barh(jr1_packages, jr1_totals, height=.8, color='green')
    plt.grid()
    plt.show() 
    
def jr1_jr5_big5_grouped_bar_chart():
    """Grouped bar chart showing comparison of jr5 vs jr1 downloads by provider in 2017 for the big 5 providers.
    Big 5 are: Elsevier, Wiley, Springer, Taylor & Francis, Sage""" 
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()

    jr5_big5_data = []
    jr1_big5_data = []

    big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
    for i in jr5_data_by_package:
        if i[0] in big5:
            jr5_big5_data.append(i)

    for i in jr1_data_by_package:
        if i[0] in big5:
            jr1_big5_data.append(i)

    packages = [x[0] for x in jr1_big5_data]
    jr1_totals = [x[1] for x in jr1_big5_data]
    jr5_totals = [x[1] for x in jr5_big5_data]

    bar_width = .25
    
    #set position of bar on X axis
    jr1_position = np.arange(len(jr1_totals))
    jr5_position = [x + bar_width for x in jr1_position]
    
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('2017 downloads by Provider: JR1 vs. JR5')
    plt.bar(jr1_position, jr1_totals, color='blue', width=bar_width, label='JR1 downloads')
    plt.bar(jr5_position, jr5_totals, color='red', width=bar_width, label='JR5 downloads')
    plt.xticks([r+bar_width for r in range(len(packages))], packages)
    plt.xticks(rotation=90)
    

    plt.legend()            #grabs the 'label' argument from plt.bar
    plt.show()
    

def jr1_jr5_other_providers_grouped_bar_chart():
   """Grouped bar chart showing comparison of jr5 and jr1 downloads by provider inn 2017 for all providers
   outside big 5"""
       
   data = pd.read_csv('Packages.csv', skiprows=8)
    
   jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
   jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()

   jr5_big5_data = []
   jr1_big5_data = []

   big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
   for i in jr5_data_by_package:
       if i[0] not in big5:
           jr5_big5_data.append(i)

   for i in jr1_data_by_package:
       if i[0] not in big5:
           jr1_big5_data.append(i)

   packages = [x[0] for x in jr1_big5_data]
   jr1_totals = [x[1] for x in jr1_big5_data]
   jr5_totals = [x[1] for x in jr5_big5_data]

   bar_width = .25
    
   #set position of bar on X axis
   jr1_position = np.arange(len(jr1_totals))
   jr5_position = [x + bar_width for x in jr1_position]
    
   plt.figure(num=None, figsize=(8,8))
   plt.suptitle('2017 downloads by Provider: JR1 vs. JR5')
   plt.bar(jr1_position, jr1_totals, color='blue', width=bar_width, label='JR1 downloads')
   plt.bar(jr5_position, jr5_totals, color='red', width=bar_width, label='JR5 downloads')
   plt.xticks([r+bar_width for r in range(len(packages))], packages)
   plt.xticks(rotation=90)

   plt.legend()            #grabs the 'label' argument from plt.bar
   plt.show()
   
   
def jr1_by_field_by_provider(provider_name):
    """Charts JR1 downloads by field for chosen provider. User inputs provider name and dynamically generates chart for that provider"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR1 2017'].sum()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR1 Downloads by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    
    plt.grid()
    plt.show()    
   
    
def jr1_percent_field_by_provider(provider_name):
    """Charts % of JR1 downloads by field for a given provider"""
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
       
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer        

    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR1 2017'].sum().tolist()     #sum of downloads per field

    sums_by_field = list(reversed(sums_by_field))  
    
    total_downloads = sum(sums_by_field)
        
    percent_by_field = [round((i/total_downloads), 4) for i in sums_by_field]
   
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent of total JR1 downloads by field for: {provider_name}')
    plt.barh(fields, percent_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 
    
    
def jr1_fluff_checker(provider_name):
    """Checking for fluff in different providers. The hypothesis is that most packages provide a small number of 
    highly used journals and the rest are fluff that we are paying for. We will look at individual titles per package
    and see which of those make up 80% of the JR5 downloads"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)   
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
    for i in journals_data:
        if i[0] == provider_name:
            journals_data.remove(i)                 #removing aggregator column data
  
    total_jr1_downloads = 0
    total_journals = 0                         
    for i in journals_data:
        total_jr1_downloads += i[2]
        total_journals += 1
        
    jr1_tuples = [(i[0], i[2]) for i in journals_data]
    jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples
    
    running_tally = 0
    highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
    for i in jr1_tuples_sorted:
        if running_tally < (total_jr1_downloads * 0.8):
            highly_used_journals.append(i)
            running_tally += i[1]
            
#    print(highly_used_journals)
    print(f"Total JR1 downloads for provider: {provider_name} = {total_jr1_downloads}")
    print(f"{len(highly_used_journals)} of {total_journals} journals make up 80% of the use")
    
    fluff_index = ((len(highly_used_journals))/(total_journals))
    print(f"Fluff index = {fluff_index}")
    
    if fluff_index < .20:
        print("Seems fluffy to me!")
        
        
def jr1_fluff_score():
    """Produces 'fluff score' value by provider for JR1 downloads and charts each provider and its corresponding fluff index.
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
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[2]
            total_journals += 1

        jr1_tuples = [(i[0], i[2]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.8):
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
    plt.suptitle(f'JR1 Fluff Score by provider')
    plot = plt.barh(providers, fluff_score, height=.8, color='green')
    
    plot[13].set_color('red')
    plot[22].set_color('red')
    plot[23].set_color('red')
    plot[26].set_color('red')
    plot[31].set_color('red')
    
    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show() 
        

def jr1_big5_by_field(field_choice):
    """Looks at jr1 downloads by field for the big 5 providers. Charts % use by field for each of the big 5 providers"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']

    big5_data = []
    for provider_name in big5:
        provider_subset = data.loc[data['Provider'] == provider_name]
        
        provider_list = provider_subset.groupby(['Provider', 'Field'], as_index=False).sum().values.tolist()
        for i in provider_list:
            if i[1] == field_choice:
                big5_data.append((i[0], i[1], i[3]))
            

    big5_packages = [x[0] for x in big5_data]
    big5_total_by_field = [x[2] for x in big5_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Big 5 Providers, JR1 downloads by field: {field_choice}')
    plt.barh(big5_packages, big5_total_by_field, height=.8, color='green')
    plt.grid()
    plt.show()        
    


