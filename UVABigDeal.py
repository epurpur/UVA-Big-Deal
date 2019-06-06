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
    over_1000_downloads = [total for total in jr5_totals if total > 1000]
    under_1000_downloads = [total for total in jr5_totals if total < 1000]

    percent_under_1000_downloads = (len(under_1000_downloads) / len(jr5_totals))
    print(f"{len(under_1000_downloads)} of {len(jr5_totals)} providers have less than 1,000 downloads. ({round(percent_under_1000_downloads, 2)}%)")


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
    over_1000_downloads = [total for total in jr5_totals if total > 1000]
    under_1000_downloads = [total for total in jr5_totals if total < 1000]

    percent_under_1000_downloads = (len(under_1000_downloads) / len(jr5_totals))
    print(f"{len(under_1000_downloads)} of {len(jr5_totals)} providers have less than 1,000 downloads. ({round(percent_under_1000_downloads, 2)}%)")



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
    over_10000_downloads = [total for total in jr1_totals if total > 10000]
    under_10000_downloads = [total for total in jr1_totals if total < 10000]

    percent_under_10000_downloads = (len(under_10000_downloads) / len(jr1_totals))
    print(f"{len(under_10000_downloads)} of {len(jr1_totals)} providers have less than 10,000 downloads. ({round(percent_under_10000_downloads, 2)}%)")


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
    plt.suptitle('Downloads JR1 2017 (without Elsevier')
    plt.barh(jr1_packages, jr1_totals, height=.8, color='green')
    plt.show()

    jr1_totals.sort()
    over_10000_downloads = [total for total in jr1_totals if total > 10000]
    under_10000_downloads = [total for total in jr1_totals if total < 10000]

    percent_under_10000_downloads = (len(under_10000_downloads) / len(jr1_totals))
    print(f"{len(under_10000_downloads)} of {len(jr1_totals)} providers have less than 10,000 downloads. ({round(percent_under_10000_downloads, 2)}%)")

read_jr1_no_elsevier()