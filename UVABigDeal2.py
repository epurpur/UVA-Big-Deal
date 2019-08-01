
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np


def percent_references_uva_authors():
    """Percent UVA references by provider by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    ex: (Elsevier UVA references 2008 / total references 2008) """
    

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    providers = ['Wiley', 'U Chicago Press', 'Taylor & Francis', 'Springer', 'Sage', 'SPIE', 'Royal Society of Chemistry', 'Project MUSE',
                 'ProQuest', 'Oxford UP', 'Ovid', 'Modern Language Association', 'MIT Press', 'Karger', 'JSTOR', 'IOPscience', 'IEEE', 'Gale',
                 'Emerald', 'Elsevier', 'Ebsco', 'DeGruyter', 'Cambridge UP', 'Brill', 'BioOne', 'Association for Computing Machinery', 'Annual Reviews',
                 'American Society of Mechanical Engineers', 'American Society of Civil Engineers', 'American Physical Society', 'American Mathematical Society',
                 'American Institute of Aeronautics and Astronautics', 'American Chemical Society', 'AIP']
                 
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    sum_2008 = 0
    sum_2009 = 0
    sum_2010 = 0
    sum_2011 = 0
    sum_2012 = 0
    sum_2013 = 0
    sum_2014 = 0
    sum_2015 = 0
    sum_2016 = 0
    sum_2017 = 0
    
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider.ref_2009.tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider.ref_2010.tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider.ref_2011.tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider.ref_2012.tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider.ref_2013.tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider.ref_2014.tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider.ref_2015.tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider.ref_2016.tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider.ref_2017.tolist()
        sum_2017 += ref_2017[0]

    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))   #list of total references by year
        
    ref_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider.ref_2009.tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider.ref_2010.tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider.ref_2011.tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider.ref_2012.tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider.ref_2013.tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider.ref_2014.tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider.ref_2015.tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider.ref_2016.tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider.ref_2017.tolist()
        ref_by_year.append(ref_2017[0])
        
        ref_by_provider.append(ref_by_year)

    all_percent_by_provider_of_total_by_year = []           #for each of big 5 providers, stores list of % of UVA references each provider made up of ALL UVA references for that year

    for i in ref_by_provider:
        individual_percent_total_by_provider_per_year = []
        
        zipped = zip(totals_by_year, i)
        for i in zipped:
            individual_percent_total_by_provider_per_year.append(i[1]/i[0])
        
        all_percent_by_provider_of_total_by_year.append(individual_percent_total_by_provider_per_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']


    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of References by UVA Authors by Provider \n (as percent of all UVA references by year)')
    plt.xlabel('Year')
    plt.ylabel('Percent of References')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, all_percent_by_provider_of_total_by_year[0], label='Elsevier')
    plt.plot(years, all_percent_by_provider_of_total_by_year[1], label='Sage')
    plt.plot(years, all_percent_by_provider_of_total_by_year[2], label='Springer')
    plt.plot(years, all_percent_by_provider_of_total_by_year[3], label='Taylor & Francis')
    plt.plot(years, all_percent_by_provider_of_total_by_year[4], label='Wiley')
    
    plt.legend()
    plt.savefig('test.jpg')       #saves output to working directory
    
    
percent_references_uva_authors()