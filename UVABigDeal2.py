
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np


def papers_big5_jr80_jr90_jr95_stacked_bar():
    """Creates stacked bar plot showing jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of downloads. JR90 are journals that make up 90% of downloads.
    JR95 are journals that make up 95% of downloads. These will all be plotted together."""
    
    data = pd.read_csv('JournalsPerProvider_noJR1.csv', skiprows=8)           #reading from different file. Needs to be fixed to read from same file, but ignore 'N/A' values

    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
#    big5 = ['AIP']        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_papers = 0
        total_journals = 0                         
        for i in journals_data:
            total_papers += i[5]
            total_journals += 1
            
        paper_tuples = [(i[0], i[5]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in paper_tuples_sorted:
            if jr80_running_tally < (total_papers * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in paper_tuples_sorted:
            if jr90_running_tally < (total_papers * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in paper_tuples_sorted:
            if jr95_running_tally < (total_papers * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles with Papers by UVA Authors')
    plt.ylabel('Percent of total titles')
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
                


papers_big5_jr80_jr90_jr95_stacked_bar()


