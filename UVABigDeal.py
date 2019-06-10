#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:25:09 2019

@author: ep9k
"""

"""Source file here to show how we've been interpreting the 1figr data. Data
about UVA's big deal scholarly publication contracts. We are pulling from
JournalsPerProvider.csv"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
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
    

def percent_jr5_of_jr1():
    """Print list of providers, showing ratio of jr5 downloads as % of all downloads(jr1) in 2017"""
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    jr1_data_by_package = data.groupby(['Provider', 'Downloads JR1 2017'], as_index=False).sum().values.tolist()
    
    combined = list(zip(jr5_data_by_package, jr1_data_by_package))
    
#    print(combined[0][0][1])
#    print(combined[0][0][4])
#    print((combined[0][0][1])/(combined[0][0][4]))
    
    final_rank = []
    
    for i in combined:
        final_rank.append((i[0][0], round((i[0][1]/i[0][4]),4)))        #round to 4 decimal places
        
    final_rank_sorted = tuple(sorted(final_rank, key=itemgetter(1), reverse=True)   )
    
    print("% JR5 downloads of total downloads in 2017 (JR1) by Provider \n")
    for i in final_rank_sorted:
        print(i[0], "-" , i[1])


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
    plt.suptitle('Downloaded articles, Occurrences by Domain')
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
    plt.suptitle('Downloaded articles, Occurrences by Field')
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
    plt.suptitle('Downloaded articles, Occurrences by Field (Big5 Providers)')
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
    plt.suptitle('Downloaded articles, Occurrences by Field (Not Big5 Providers)')
    plt.barh(fields, counts, height=.8, color='green')
    plt.grid()
    plt.show() 

#read_jr5()
#read_jr5_no_elsevier()
#jr5_big5()
#jr5_other_providers()
#
#read_jr1()
#read_jr1_no_elsevier()
#jr1_big5()
#jr1_other_providers()
#
#
#jr1_jr5_big5_grouped_bar_chart() 
#jr1_jr5_other_providers_grouped_bar_chart()
#        
#percent_jr5_of_jr1()
#journals_by_domain()
#journals_by_field()

journals_by_field_big5()
journals_by_field_other_providers()





