
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np

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

        print(jr5_tuples_sorted)

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr5_tuples_sorted:
            if running_tally < (total_jr5_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
                
        jr80_score = (len(highly_used_journals))/(total_journals)
        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR80 journals")    #used to print each provider with number of journals included
                
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



big5_jr80_jr5_downloads()


