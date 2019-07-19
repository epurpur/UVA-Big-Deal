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
   
    
def big5_percent_jr5_of_jr1():
    """A measurement of currency. Compares JR5 downloads to JR1 downloads for each of the big 5 providers.
    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading."""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
#    big5 = ['AIP', 'American Chemical Society']
    
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
        
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - .0175,           #sets x axis position of labels
                 i.get_y() + .35,
                 '{:.2%}'.format(score),
                 ha='center',
                 va='center') 
        
    
def scopus_uva_publications_2017():
    """Using Scopus data, computes total UVA publications vs total publications by provider. Data is only 2017 data."""
    
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
    providers = [i[0] for i in providers]

    all_provider_scores = []
    
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        papers_2017 = subset_by_provider.papers_2017.tolist()
        papers_2017 = papers_2017[0]  #first number in list is sum of rest of numbers
             #to avoid 'divide by 0' error
        
        
        total_2017 = subset_by_provider.total_2017.tolist()
        total_2017 = total_2017[0]
        if total_2017 is 0:
            total_2017 = 0.1               #to avoid 'divide by 0' error
        
        print(f"{provider_name} : {papers_2017} of {total_2017} papers are UVA publications in 2017" )
        provider_score = papers_2017/total_2017   

        all_provider_scores.append((provider_name, provider_score))  #tie the provider_name and publisher score together

    all_provider_scores = sorted(all_provider_scores, key=itemgetter(1), reverse=True)
    
    providers = [x[0] for x in all_provider_scores]
    provider_score = [x[1] for x in all_provider_scores]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8)) 
    plt.suptitle('UVA publications as % of total publications (2017 Scopus Data)')
    plot = plt.barh(providers, provider_score, height=.8, color='green')
    
    #red color for the big 5
    plot[8].set_color('red')
    plot[11].set_color('red')
    plot[12].set_color('red')
    plot[16].set_color('red')
    plot[18].set_color('red')

    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show()


def scopus_uva_publications_all_years():
    """Using Scopus data, computes total UVA publications vs total publications for all years by provider. Data is for a 10 year period (2008-2017)"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
    providers = [i[0] for i in providers]

    all_provider_scores = []

    for provider_name in providers:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        papers = subset_by_provider.Papers.tolist()
        total_uva_publications = papers[0]   #first item in list is total # of publications for 10 year period of Scopus data

        total_papers_scopus = []

        total_2008 = subset_by_provider.total_2008.tolist()
        total_papers_scopus.append(total_2008[0])
        total_2009 = subset_by_provider.total_2009.tolist()
        total_papers_scopus.append(total_2009[0])
        total_2010 = subset_by_provider.total_2010.tolist()
        total_papers_scopus.append(total_2010[0])
        total_2011 = subset_by_provider.total_2011.tolist()
        total_papers_scopus.append(total_2011[0])
        total_2012 = subset_by_provider.total_2012.tolist()
        total_papers_scopus.append(total_2012[0])
        total_2013 = subset_by_provider.total_2013.tolist()
        total_papers_scopus.append(total_2013[0])
        total_2014 = subset_by_provider.total_2014.tolist()
        total_papers_scopus.append(total_2014[0])
        total_2015 = subset_by_provider.total_2015.tolist()
        total_papers_scopus.append(total_2015[0])
        total_2016 = subset_by_provider.total_2016.tolist()
        total_papers_scopus.append(total_2016[0])
        total_2017 = subset_by_provider.total_2017.tolist()
        total_papers_scopus.append(total_2017[0])

        grand_total = sum(total_papers_scopus)

        provider_score = total_uva_publications/grand_total
        all_provider_scores.append((provider_name, provider_score))  #tie the provider_name and publisher score together
    
    all_provider_scores = sorted(all_provider_scores, key=itemgetter(1), reverse=True)

    providers = [x[0] for x in all_provider_scores]
    provider_score = [x[1] for x in all_provider_scores]

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8)) 
    plt.suptitle('UVA publications as % of total publications (2008-2017 All Years Scopus Data)')
    plot = plt.barh(providers, provider_score, height=.8, color='green')
    
    #red color for the big 5
    plot[13].set_color('red')
    plot[21].set_color('red')
    plot[27].set_color('red')
    plot[28].set_color('red')
    plot[29].set_color('red')

    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show()
    
   
def citations_by_discipline(provider_name):
    """Shows distribution of citations by discipline for the specified provider.
    Citations are a reference to any paper authored by a UVA affiliated author.
    However, if multiple UVA authors collaborate on one paper, this counts for only one citation.
    'Disciplines' is a column we derived from the pre-existing 'fields' column in the 1figr data.
    Disciplines has mapped those field categories into more UVA specific language"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]

    disciplines_data = subset_by_provider.groupby(['Discipline'], as_index=False).sum().values.tolist()

    disciplines = []
    citation_totals = []
    
    for i in disciplines_data:
        discipline_name = i[0]
        disciplines.append(discipline_name)
        discipline_citations = i[4]
        citation_totals.append(discipline_citations)      #int() to remove decimal points

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Distribution of Citations by Discipline for Provider: {provider_name} \n (Disciplines are specific to UVA)')
    plot = plt.barh(disciplines, citation_totals, height=.8, color='green')    
        
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() + 2300,           #sets x axis position of labels
                 i.get_y() + .35,
                 score,
                 ha='center',
                 va='center')


def publications_by_discipline(provider_name):
    """Shows distribution of publications by discipline for the specified provider.
    Publications are publications by any UVA affiliated author.
    However if multiple UVA authors collaborate on one paper, this counts for only one publication.
    'Disciplines' is a column we derived from the pre-existing 'fields' column in the 1figr data.
    Disciplines has mapped those field categories into more UVA specific language"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]

    disciplines_data = subset_by_provider.groupby(['Discipline'], as_index=False).sum().values.tolist()

    disciplines = []
    publication_totals = []
    
    for i in disciplines_data:
        discipline_name = i[0]
        disciplines.append(discipline_name)
        discipline_publications = i[5]
        publication_totals.append(discipline_publications)      #int() to remove decimal points

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Distribution of Publications by Discipline for Provider: {provider_name} \n (Disciplines are specific to UVA)')
    plot = plt.barh(disciplines, publication_totals, height=.8, color='green')    
        
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() + 90,           #sets x axis position of labels
                 i.get_y() + .35,
                 score,
                 ha='center',
                 va='center') 




