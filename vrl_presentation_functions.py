#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:39:38 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np
from pylab import *


"""Functions that will be presented at the VRL meeting, august 5"""

def big5_jr80_jr1_downloads():
    """Produces 'JR80' value by provider for JR1 downloads and charts each provider and its corresponding JR80 value.
    JR80 is defined as: "Journals representing 80% of downloads for their respective provider"
    Here is how JR80 score is calculated:
        - Cleaned 'N/A' values from 'JR1..' column to remove no data values     #NEED TO FIX THIS LATER
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates JR80 score as number of journals required to reach 80% / total journals by provider
        - Plots JR80 score of all providers"""

    data = pd.read_csv('JournalsPerProvider_noJR1.csv', skiprows=8)           #reading from different file. Needs to be fixed to read from same file, but ignore 'N/A' values

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']  

    jr80_by_provider = []
    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:
        
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
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
                
        jr80_score = (len(highly_used_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR80 journals")    #used to print each provider with number of journals included
                
        jr80_by_provider.append((provider_name, jr80_score))
        plot_stats_by_provider.append((provider_name, jr80_score, f'{len(highly_used_journals)}/{total_journals}'))
        
    jr80_by_provider = sorted(jr80_by_provider, key=itemgetter(1), reverse=True)
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)     #sorting to match order of jr80_scores
    
    
    providers = [x[0] for x in jr80_by_provider]
    jr80_value = [x[1] for x in jr80_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]   #this is used for labels in final plot

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage JR80 Titles by Provider \n(# Journals from all years downloaded in 2017 which account for 80% of use)')

    plot = plt.barh(providers, jr80_value, height=.8, color='green')
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() - .022,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
    plt.show()


def big5_jr90_jr1_downloads():
    """Produces 'JR90' value by provider for JR1 downloads and charts each provider and its corresponding JR90 value.
    JR90 is defined as: "Journals representing 90% of downloads for their respective provider"
    Here is how JR90 score is calculated:
        - Cleaned 'N/A' values from 'JR1..' column to remove no data values     #NEED TO FIX THIS LATER
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 90% of total jr1 downloads
        - Calculates JR90 score as number of journals required to reach 90% / total journals by provider
        - Plots JR90 score of all providers"""

    data = pd.read_csv('JournalsPerProvider_noJR1.csv', skiprows=8)           #reading from different file. Needs to be fixed to read from same file, but ignore 'N/A' values

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']  

    jr90_by_provider = []
    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:
        
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
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.9):
                highly_used_journals.append(i)
                running_tally += i[1]
                
        jr90_score = (len(highly_used_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR90 journals")    #used to print each provider with number of journals included
                
        jr90_by_provider.append((provider_name, jr90_score))
        plot_stats_by_provider.append((provider_name, jr90_score, f'{len(highly_used_journals)}/{total_journals}'))
        
    jr90_by_provider = sorted(jr90_by_provider, key=itemgetter(1), reverse=True)
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)     #sorting to match order of jr80_scores
    
    
    providers = [x[0] for x in jr90_by_provider]
    jr90_value = [x[1] for x in jr90_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]   #this is used for labels in final plot

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage JR90 Titles by Provider \n(# Journals from all years downloaded in 2017 which account for 90% of use)')

    plot = plt.barh(providers, jr90_value, height=.8, color='green')
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() - .022,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
    plt.show()


def big5_jr95_jr1_downloads():
    """Produces 'JR95' value by provider for JR1 downloads and charts each provider and its corresponding JR95 value.
    JR95 is defined as: "Journals representing 95% of downloads for their respective provider"
    Here is how JR95 score is calculated:
        - Cleaned 'N/A' values from 'JR1..' column to remove no data values     #NEED TO FIX THIS LATER
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 95% of total jr1 downloads
        - Calculates JR95 score as number of journals required to reach 95% / total journals by provider
        - Plots JR95 score of all providers"""

    data = pd.read_csv('JournalsPerProvider_noJR1.csv', skiprows=8)           #reading from different file. Needs to be fixed to read from same file, but ignore 'N/A' values

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']  

    jr95_by_provider = []
    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:
        
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
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.95):
                highly_used_journals.append(i)
                running_tally += i[1]
                
        jr95_score = (len(highly_used_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR95 journals")    #used to print each provider with number of journals included
                
        jr95_by_provider.append((provider_name, jr95_score))
        plot_stats_by_provider.append((provider_name, jr95_score, f'{len(highly_used_journals)}/{total_journals}'))
        
    jr95_by_provider = sorted(jr95_by_provider, key=itemgetter(1), reverse=True)
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)     #sorting to match order of jr80_scores
    
    
    providers = [x[0] for x in jr95_by_provider]
    jr95_value = [x[1] for x in jr95_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]   #this is used for labels in final plot

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage JR95 Titles by Provider \n(# Journals from all years downloaded in 2017 which account for 95% of use)')

    plot = plt.barh(providers, jr95_value, height=.8, color='green')
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() - .035,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
    plt.show()


def big5_jr80_jr5_downloads():
    """Produces 'JR80' value by provider for JR5 downloads and charts each provider and its corresponding JR80 value.
    JR80 is defined as: "Journals representing 80% of downloads for their respective provider"
    Here is how JR80 score is calculated:
        - Cleaned 'N/A' values from 'JR1..' column to remove no data values     #NEED TO FIX THIS LATER
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates JR80 score as number of journals required to reach 80% / total journals by provider
        - Plots JR80 score of all providers"""

    data = pd.read_csv('JournalsPerProvider_noJR5.csv', skiprows=8)           #reading from different file. Needs to be fixed to read from same file, but ignore 'N/A' values

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']  
#    big5=['AIP']
    jr80_by_provider = []
    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:
        
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
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr5_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr5_tuples_sorted:
            if running_tally < (total_jr5_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
                
        jr80_score = (len(highly_used_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR80 journals")    #used to print each provider with number of journals included
                
        jr80_by_provider.append((provider_name, jr80_score))
        plot_stats_by_provider.append((provider_name, jr80_score, f'{len(highly_used_journals)}/{total_journals}'))
        
    jr80_by_provider = sorted(jr80_by_provider, key=itemgetter(1), reverse=True)
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)     #sorting to match order of jr80_scores
    
    
    providers = [x[0] for x in jr80_by_provider]
    jr80_value = [x[1] for x in jr80_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]   #this is used for labels in final plot

    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percentage JR80 Titles by Provider \n(2017 downloads in 2017 which account for 80% of use)')

    plot = plt.barh(providers,jr80_value, height=.8, color='green')
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() - .022,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
    plt.show()


def big5_ref80_references():
    """For those titles that make up 80% of the references (ref80_score, same as JR80 but for references). 
    We want to number of titles that make up 80% of the references."""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
    
    ref80_by_provider = []
    plot_stats_by_provider = []    #used later for labels in plot
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for journal in journals_data:
            if journal[0] == provider_name:
                journals_data.remove(journal)
                     
        total_references = 0
        total_journals = 0
        for journal in journals_data:
            total_references += journal[4]
            total_journals += 1
            
        reference_tuples = [(i[0], i[4]) for i in journals_data]
        reference_tuples_sorted = sorted(reference_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of reference_tuples

        running_tally = 0
        highly_referenced_journals = []            #this holds (journal name, references)
        for journal in reference_tuples_sorted:
            if running_tally < (total_references * 0.8):
                highly_referenced_journals.append(journal)
                running_tally += journal[1]
        

        ref80_score = (len(highly_referenced_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_referenced_journals)} of {total_journals} are ref80 journals")    #used to print each provider with number of journals included
        
        ref80_by_provider.append((provider_name, ref80_score))
        plot_stats_by_provider.append((provider_name, ref80_score, f'{len(highly_referenced_journals)}/{total_journals}'))
        
    ref80_by_provider = sorted(ref80_by_provider, key=itemgetter(1), reverse=True)   #sorting by ref80 score
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)    #sorting to match order of ref80 scores
    
    providers = [x[0] for x in ref80_by_provider]
    ref80_value = [x[1] for x in ref80_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]     #this is to use for labels in final chart

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percent References to Provider Titles \n(# Journals which account for 80% of references)')
    plot = plt.barh(providers, ref80_value, height=.8, color='green')
    
    element_number = 0                          #needed to count to get correct index to include for plot label
    for i in plot:
        plt.text(i.get_width() - .015,        #sets x axis position of labels
                 i.get_y() + .35,
                 plot_stats[element_number],      
                 ha='center',
                 va='center')
        element_number += 1
    
    
def big5_pap80_papers():
    """For those titles that make up 80% of the publications (pap80_score, same as JR80 but for references). 
    We want to number of titles that make up 80% of the references."""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
    
    pap80_by_provider = []
    plot_stats_by_provider = []     #used later for labels in plot
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for journal in journals_data:
            if journal[0] == provider_name:
                journals_data.remove(journal)
                     
        total_papers = 0
        total_journals = 0
        for journal in journals_data:
            total_papers += journal[5]
            total_journals += 1
            
        paper_tuples = [(i[0], i[5]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of reference_tuples

        running_tally = 0
        highly_published_journals = []            #this holds (journal name, references)
        for journal in paper_tuples_sorted:
            if running_tally < (total_papers * 0.8):
                highly_published_journals.append(journal)
                running_tally += journal[1]
        

        pap80_score = (len(highly_published_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_published_journals)} of {total_journals} are pap80 journals")    #used to print each provider with number of journals included
        
        pap80_by_provider.append((provider_name, pap80_score))
        plot_stats_by_provider.append((provider_name, pap80_score, f'{len(highly_published_journals)}/{total_journals}'))
        
    pap80_by_provider = sorted(pap80_by_provider, key=itemgetter(1), reverse=True)   #sorting by ref80 score
    plot_stats_by_provider = sorted(plot_stats_by_provider, key=itemgetter(1), reverse=True)    #sorting to match order of pap80 scores
    
    providers = [x[0] for x in pap80_by_provider]
    pap80_value = [x[1] for x in pap80_by_provider]
    plot_stats = [x[2] for x in plot_stats_by_provider]     #this is to use for labels in final chart


    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'% Publications to Provider Titles \n(# Journals which account for 80% of publications)')
    plot = plt.barh(providers, pap80_value, height=.8, color='green')
    
    element_number = 0                          #needed to count to get correct index to include for plot label
    for i in plot:
        plt.text(i.get_width() - .015,        #sets x axis position of labels
                 i.get_y() + .35,
                 plot_stats[element_number],      
                 ha='center',
                 va='center')
        element_number += 1


def number_uva_papers_over_time():
    """Plots # of UVA authored publications in each of the big 5 providers over time (2008-2017)
    Looks at columns under 'Papers per journal/provider by your institution's authors"""

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']
    
    publications_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        publications_by_year = []
        
        papers_2008 = subset_by_provider.papers_2008.tolist()
        publications_by_year.append(papers_2008[0])
        papers_2009 = subset_by_provider.papers_2009.tolist()
        publications_by_year.append(papers_2009[0])
        papers_2010 = subset_by_provider.papers_2010.tolist()
        publications_by_year.append(papers_2010[0])
        papers_2011 = subset_by_provider.papers_2011.tolist()
        publications_by_year.append(papers_2011[0])
        papers_2012 = subset_by_provider.papers_2012.tolist()
        publications_by_year.append(papers_2012[0])
        papers_2013 = subset_by_provider.papers_2013.tolist()
        publications_by_year.append(papers_2013[0])
        papers_2014 = subset_by_provider.papers_2014.tolist()
        publications_by_year.append(papers_2014[0])
        papers_2015 = subset_by_provider.papers_2015.tolist()
        publications_by_year.append(papers_2015[0])
        papers_2016 = subset_by_provider.papers_2016.tolist()
        publications_by_year.append(papers_2016[0])
        papers_2017 = subset_by_provider.papers_2017.tolist()
        publications_by_year.append(papers_2017[0])
        
        publications_by_provider.append(publications_by_year)
            
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Number of UVA Authored Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')

    #change this to be dynamic instead of hard coded
    plt.plot(years, publications_by_provider[0], label='Elsevier')
    plt.plot(years, publications_by_provider[1], label='Taylor & Francis')
    plt.plot(years, publications_by_provider[2], label='Sage')
    plt.plot(years, publications_by_provider[3], label='Springer')
    plt.plot(years, publications_by_provider[4], label='Wiley')
    
    plt.legend()


def percent_uva_papers_over_time():
    """Plots percentage of UVA authored papers in each of the big 5 providers over time (2008-2017)
    Divides # UVA authored papers for current year by total number of papers in that journal.
    For example, this is 'papers_2008' / total_2008"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']

    percentage_by_provider = []
    
    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        percentage_per_year = []
        
        uva_2008 = subset_by_provider.papers_2008.tolist()
        total_2008 = subset_by_provider.total_2008.tolist()
        percentage_per_year.append(uva_2008[0] / total_2008[0])
        
        uva_2009 = subset_by_provider.papers_2009.tolist()
        total_2009 = subset_by_provider.total_2009.tolist()
        percentage_per_year.append(uva_2009[0] / total_2009[0])
        
        uva_2010 = subset_by_provider.papers_2010.tolist()
        total_2010 = subset_by_provider.total_2010.tolist()
        percentage_per_year.append(uva_2010[0] / total_2010[0])
        
        uva_2011 = subset_by_provider.papers_2011.tolist()
        total_2011 = subset_by_provider.total_2011.tolist()
        percentage_per_year.append(uva_2011[0] / total_2011[0])
        
        uva_2012 = subset_by_provider.papers_2012.tolist()
        total_2012 = subset_by_provider.total_2012.tolist()
        percentage_per_year.append(uva_2012[0] / total_2012[0])
        
        uva_2013 = subset_by_provider.papers_2013.tolist()
        total_2013 = subset_by_provider.total_2013.tolist()
        percentage_per_year.append(uva_2013[0] / total_2013[0])
        
        uva_2014 = subset_by_provider.papers_2014.tolist()
        total_2014 = subset_by_provider.total_2014.tolist()
        percentage_per_year.append(uva_2014[0] / total_2014[0])
        
        uva_2015 = subset_by_provider.papers_2015.tolist()
        total_2015 = subset_by_provider.total_2015.tolist()
        percentage_per_year.append(uva_2015[0] / total_2015[0])
        
        uva_2016 = subset_by_provider.papers_2016.tolist()
        total_2016 = subset_by_provider.total_2016.tolist()
        percentage_per_year.append(uva_2016[0] / total_2016[0])
        
        uva_2017 = subset_by_provider.papers_2017.tolist()
        total_2017 = subset_by_provider.total_2017.tolist()
        percentage_per_year.append(uva_2017[0] / total_2017[0])
        
        percentage_by_provider.append(percentage_per_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
       
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage of UVA Authored Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Percent of Total Publications')

    plt.plot(years, percentage_by_provider[0], label='Elsevier')
    plt.plot(years, percentage_by_provider[1], label='Taylor & Francis')
    plt.plot(years, percentage_by_provider[2], label='Sage')
    plt.plot(years, percentage_by_provider[3], label='Springer')
    plt.plot(years, percentage_by_provider[4], label='Wiley')
    
    plt.legend()


def oa_percent_papers_available_over_time():
    """Percent of papers available Open Access (oa) for each of the big 5 providers over time (2008-2017)
    Looks at columns under '% of OA papers in 1findr per journal/provider (intersection with Scopus)"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']
    
    oa_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        oa_by_year = []

        oa_2008 = subset_by_provider.oa_2008.tolist()
        oa_by_year.append(oa_2008[0])
        oa_2009 = subset_by_provider.oa_2009.tolist()
        oa_by_year.append(oa_2009[0])
        oa_2010 = subset_by_provider.oa_2010.tolist()
        oa_by_year.append(oa_2010[0])
        oa_2011 = subset_by_provider.oa_2011.tolist()
        oa_by_year.append(oa_2011[0])
        oa_2012 = subset_by_provider.oa_2012.tolist()
        oa_by_year.append(oa_2012[0])
        oa_2013 = subset_by_provider.oa_2013.tolist()
        oa_by_year.append(oa_2013[0])
        oa_2014 = subset_by_provider.oa_2014.tolist()
        oa_by_year.append(oa_2014[0])
        oa_2015 = subset_by_provider.oa_2015.tolist()
        oa_by_year.append(oa_2015[0])
        oa_2016 = subset_by_provider.oa_2016.tolist()
        oa_by_year.append(oa_2016[0])
        oa_2017 = subset_by_provider.oa_2017.tolist()
        oa_by_year.append(oa_2017[0])
        
        oa_by_provider.append(oa_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
        
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage of OA-Available Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Percent Available')
    
    plt.plot(years, oa_by_provider[0], label='Elsevier')
    plt.plot(years, oa_by_provider[1], label='Taylor & Francis')
    plt.plot(years, oa_by_provider[2], label='Sage')
    plt.plot(years, oa_by_provider[3], label='Springer')
    plt.plot(years, oa_by_provider[4], label='Wiley')
    
    plt.legend()
     

def oa_number_papers_available_over_time():
    """Number of papers available Open Access (oa) for each of the big 5 providers over time (2008-2017)
    Looks at columns under 'OA papers in 1finder per journal/provider (Intersection with scopus)"""

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']
#    big5 = ['AIP']
    oa_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        oa_by_year = []
    
        oa_2008 = subset_by_provider.oa_papers_2008.tolist()
        oa_by_year.append(oa_2008[0])
        oa_2009 = subset_by_provider.oa_papers_2009.tolist()
        oa_by_year.append(oa_2009[0])
        oa_2010 = subset_by_provider.oa_papers_2010.tolist()
        oa_by_year.append(oa_2010[0])
        oa_2011 = subset_by_provider.oa_papers_2011.tolist()
        oa_by_year.append(oa_2011[0])
        oa_2012 = subset_by_provider.oa_papers_2012.tolist()
        oa_by_year.append(oa_2012[0])
        oa_2013 = subset_by_provider.oa_papers_2013.tolist()
        oa_by_year.append(oa_2013[0])
        oa_2014 = subset_by_provider.oa_papers_2014.tolist()
        oa_by_year.append(oa_2014[0])
        oa_2015 = subset_by_provider.oa_papers_2015.tolist()
        oa_by_year.append(oa_2015[0])
        oa_2016 = subset_by_provider.oa_papers_2016.tolist()
        oa_by_year.append(oa_2016[0])
        oa_2017 = subset_by_provider.oa_papers_2017.tolist()
        oa_by_year.append(oa_2017[0])
        
        oa_by_provider.append(oa_by_year)
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of OA-Available Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Number Papers Available')

    plt.plot(years, oa_by_provider[0], label='Elsevier')
    plt.plot(years, oa_by_provider[1], label='Taylor & Francis')
    plt.plot(years, oa_by_provider[2], label='Sage')
    plt.plot(years, oa_by_provider[3], label='Springer')
    plt.plot(years, oa_by_provider[4], label='Wiley')

    plt.legend()
    

def big5_percent_jr5_of_jr1():
    """A measurement of currency. Compares JR5 downloads to JR1 downloads for each of the big 5 providers.
    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading."""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
    
    percent_jr5_of_jr1 = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[2]
                jr5_total = i[3]
                ratio = jr5_total/jr1_total
                percent_jr5_of_jr1.append(ratio)
                
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads \n (Measures currency of article use)')
    plot = plt.barh(big5, percent_jr5_of_jr1, height=.8, color='green')    
    plt.xlim(0, 1)  #changes left and right limit of x axis in plot

        
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - .034,           #sets x axis position of labels
                 i.get_y() + .35,
                 '{:.1%}'.format(score),
                 ha='center',
                 va='center') 
    
    
def number_oa_papers_by_discipline(provider_name):
    """Plots Open Access (oa) papers by discipline for the given provider.
    Discipline is a UVA-specific column. Mapped from 'field'.
    This gets a provider as an argument, finds all the unique disciplines within that provider
    then iterates through each year over the 10 year scopus data (2008-2017) and adds # of OA
    publications to each discipline to get the total per discipline."""

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           

    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    disciplines_data = subset_by_provider.groupby(['Discipline'], as_index=False).sum().values.tolist()
    
    oa_info_by_provider = []
    
    for i in disciplines_data:
        discipline_name = i[0]
        oa_papers = i[31] + i[32] + i[33] + i[34] + i[35] + i[36] + i[37] + i[38] + i[39] + i[40]       #index for each column oa_papers_2008 + oa_papers_2009...
        oa_info_by_provider.append((discipline_name, oa_papers))
    
    oa_info_by_provider = sorted(oa_info_by_provider, key=itemgetter(0), reverse=True)      #sorts in reverse alphabetical order 
    disciplines = [x[0] for x in oa_info_by_provider]
    oa_papers_total = [x[1] for x in oa_info_by_provider]
    
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Number Open Access papers for provider: {provider_name}')
    
    plot = plt.barh(disciplines, oa_papers_total, color='green')
    plt.xlim(0,450000)    #changes left and right limit of x axis in plot
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() + 20000,
                 i.get_y() + .35,
                 score,
                 ha='center',
                 va='center')    
        

def percentage_oa_papers_by_discipline(provider_name):
    """Plots percentage Open Access (OA) papers by discipline for given provider.
    This is percentage open access papers of total papers by discipline.
    Discipline is a UVA-specific column. Mapped from 'field'.
    This sums total OA papers and divides that by total papers for each discipline, for the given provider"""
   
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           

    subset_by_provider = data.loc[data['Provider'] == provider_name]

    disciplines_data = subset_by_provider.groupby(['Discipline'], as_index=False).sum().values.tolist()
                 
    oa_info_by_provider = []
        
    for i in disciplines_data:
        discipline_name = i[0]
        oa_papers = i[31] + i[32] + i[33] + i[34] + i[35] + i[36] + i[37] + i[38] + i[39] + i[40]       #index for each column oa_papers_2008 + oa_papers_2009...
        total_papers = i[51] + i[52] + i[53] + i[54] + i[55] + i[56] + i[57] + i[58] + i[59] + i[60]
        oa_info_by_provider.append((discipline_name, oa_papers, total_papers))
        
        
    oa_info_by_provider = sorted(oa_info_by_provider, key=itemgetter(0), reverse=True)
    disciplines = [x[0] for x in oa_info_by_provider]
    oa_percentage_by_discipline = [x[1]/x[2] for x in oa_info_by_provider]
    
    plot_stats = []
    for i in oa_info_by_provider:
        plot_stats.append(f'{i[1]} / {i[2]}')
    

    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Open Access Papers as Percentage of Total Papers in Discipline for Provider: {provider_name}')
    
    plot = plt.barh(disciplines, oa_percentage_by_discipline, color='green')
    plt.xlim(0, 1)  #changes left and right limit of x axis in plot
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() + .1,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
        
def big5_cost_per_jr1_download():
    """Using cost data per provider, plots cost per jr1 download for each provider. Divides total package
    price by total number of JR1 downloads. JR1 downloads are all years' downloads in current year.
    Fix this to incorporate the usual csv reading the data instead of hard coded values"""

    downloads_info = []

    cost_per_provider = {
                    'Elsevier' : [2340568.00, 153142],
                    'Sage' : [207700.00, 9810],
                    'Wiley' : [1016814.29, 36531],
                    'Springer' : [928223.19, 32909],
                    'Taylor & Francis' : [95475.00, 7135]}  
    
    for provider_name, values in cost_per_provider.items():
        package_cost = values[0]
        jr1_downloads = values[1]
        cost_per_download = package_cost/jr1_downloads
        downloads_info.append((provider_name, cost_per_download))
        
    providers = [x[0] for x in downloads_info]
    cost = [x[1] for x in downloads_info]
    
    
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Big5 Providers Cost Per JR5 Download\n Package Cost/# of JR5 Downloads')
    plt.xlabel('Dollars')
                 
    plot = plt.barh(providers, cost, color='green')
    
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - 3,
                 i.get_y() + .35,
                 '${:,.2f}'.format(score),
                 ha='center',
                 va='center')
    
        
    
    
    

    
    
    
        
    