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
    plt.show()

    jr5_totals.sort()
    over_5000_downloads = [total for total in jr5_totals if total > 5000]
    under_5000_downloads = [total for total in jr5_totals if total < 5000]

    percent_under_5000_downloads = (len(under_5000_downloads) / len(jr5_totals))
    print(f"{len(under_5000_downloads)} of {len(jr5_totals)} providers have less than 5,000 downloads. ({round(percent_under_5000_downloads, 2)}%)")


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
    plt.show()

    jr5_totals.sort()
    over_5000_downloads = [total for total in jr5_totals if total > 5000]
    under_5000_downloads = [total for total in jr5_totals if total < 5000]

    percent_under_5000_downloads = (len(under_5000_downloads) / len(jr5_totals))
    print(f"{len(under_5000_downloads)} of {len(jr5_totals)} providers have less than 5,000 downloads. ({round(percent_under_5000_downloads, 2)}%)")


def jr5_more_than_10k_downloads():
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()
    big5_data = []

    #could only get it to work correctly by explicitly calling these strings for each provider name
    for i in jr5_data_by_package:
        if i[0] == 'Elsevier':
            big5_data.append(i)
        elif i[0] == 'Wiley':
            big5_data.append(i)
        elif i[0] == 'Ovid':
            big5_data.append(i)
        elif i[0] == 'American Chemical Society':
            big5_data.append(i)
        elif i[0] == 'Springer':
            big5_data.append(i)
        elif i[0] == 'IEEE':
            big5_data.append(i)

    
    big5_packages = [x[0] for x in big5_data]
    big5_totals = [x[1] for x in big5_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017 (>10k Downloads)')
    plt.barh(big5_packages, big5_totals, height=.8, color='green')
    plt.show()
    
    
def jr5_less_than_10k_downloads():
    
    data = pd.read_csv('Packages.csv', skiprows=8)
    
    jr5_data_by_package = data.groupby(['Provider', 'Downloads JR5 2017 in 2017'], as_index=False).sum().values.tolist()

    #could only get it to work correctly by explicitly calling these strings for each provider name
    for i in jr5_data_by_package:
        if i[0] == 'Elsevier':
            jr5_data_by_package.remove(i)
        elif i[0] == 'Wiley':
            jr5_data_by_package.remove(i)
        elif i[0] == 'Ovid':
            jr5_data_by_package.remove(i)
        elif i[0] == 'American Chemical Society':
            jr5_data_by_package.remove(i)
        elif i[0] == 'Springer':
            jr5_data_by_package.remove(i)
        elif i[0] == 'IEEE':
            jr5_data_by_package.remove(i)
            
    
    jr5_packages = [x[0] for x in jr5_data_by_package]
    jr5_totals = [x[1] for x in jr5_data_by_package]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Downloads JR5 2017 in 2017 (<10k Downloads)')
    plt.barh(jr5_packages, jr5_totals, height=.8, color='green')
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
    plt.show()

    jr1_totals.sort()
    over_100k_downloads = [total for total in jr1_totals if total > 100000]
    under_100k_downloads = [total for total in jr1_totals if total < 100000]

    percent_under_100k_downloads = (len(under_100k_downloads) / len(jr1_totals))
    print(f"{len(under_100k_downloads)} of {len(jr1_totals)} providers have less than 100,000 downloads. ({round(percent_under_100k_downloads, 2)}%)")


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
    plt.show()

    jr1_totals.sort()
    over_100k_downloads = [total for total in jr1_totals if total > 100000]
    under_100k_downloads = [total for total in jr1_totals if total < 100000]

    percent_under_100k_downloads = (len(under_100k_downloads) / len(jr1_totals))
    print(f"{len(under_100k_downloads)} of {len(jr1_totals)} providers have less than 100,000 downloads. ({round(percent_under_100k_downloads, 2)}%)")




#read_jr5()
#read_jr5_no_elsevier()
jr5_more_than_10k_downloads()
jr5_less_than_10k_downloads() 
#read_jr1()
#read_jr1_no_elsevier()







