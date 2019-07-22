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


"""Functions that will be presented at the VRL meeting, august 5"""



def big5_ref80_references():
    """For those titles that make up 80% of the references (ref80_score, same as JR80 but for references). We want to number of titles that
    make up 80% of the references. Show % of x axis, and raw numbers in label for each bar (ex: (80/250))"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
#    big5 = ['AIP']
    
    ref80_by_provider = []
    
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
        print(f"{provider_name} : {len(highly_referenced_journals)} of {total_journals} are ref80 journals")    #used to print each provider with number of journals included
        
        ref80_by_provider.append((provider_name, ref80_score))
        
    ref80_by_provider = sorted(ref80_by_provider, key=itemgetter(1), reverse=True)   #sorting by ref80 score
    
    providers = [x[0] for x in ref80_by_provider]
    ref80_value = [x[1] for x in ref80_by_provider]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'References to Provider Titles \n(# titles which account for 80% of references)')
    plot = plt.barh(providers, ref80_value, height=.8, color='green')
    
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - .015,        #sets x axis position of labels
                 i.get_y() + .35,
                 '{:.1%}'.format(score),      #Fix this!
                 ha='center',
                 va='center')
    
    
def big5_pap80_papers():
    """For those titles that make up 80% of the publications (pap80_score, same as JR80 but for references). We want to number of titles that
    make up 80% of the references. Show % of x axis, and raw numbers in label for each bar (ex: (80/250))"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
#    big5 = ['AIP']
    
    pap80_by_provider = []
    
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
        print(f"{provider_name} : {len(highly_published_journals)} of {total_journals} are ref80 journals")    #used to print each provider with number of journals included
        
        pap80_by_provider.append((provider_name, pap80_score))
        
    pap80_by_provider = sorted(pap80_by_provider, key=itemgetter(1), reverse=True)   #sorting by ref80 score
    
    providers = [x[0] for x in pap80_by_provider]
    pap80_value = [x[1] for x in pap80_by_provider]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Publications to Provider Titles \n(# titles which account for 80% of papers)')
    plot = plt.barh(providers, pap80_value, height=.8, color='green')
    
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - .015,        #sets x axis position of labels
                 i.get_y() + .35,
                 '{:.1%}'.format(score),       ###Fix this!
                 ha='center',
                 va='center')

big5_ref80_references()
big5_pap80_papers()
