
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np



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
        plot_stats.append(f'{i[1]}/{i[2]}')
    

    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Open Access Papers as Percentage of Total Papers in Discipline for Provider: {provider_name}')
    
    plot = plt.barh(disciplines, oa_percentage_by_discipline, color='green')
    plt.xlim(0, .62)  #changes left and right limit of x axis in plot
    
    element_number = 0
    for i in plot:
        plt.text(i.get_width() + .07,
                 i.get_y() + .35,
                 plot_stats[element_number],
                 ha='center',
                 va='center')
        element_number += 1
        
    plt.show()


percentage_oa_papers_by_discipline('Elsevier')


