import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np


data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
providers = [i[0] for i in providers]

subset_by_provider = data.loc[data['Provider'] == 'AIP']

papers_2017 = subset_by_provider.papers_2017.tolist()
papers_2017 = papers_2017[0]  #first number in list is sum of rest of numbers

total_2017 = subset_by_provider.total_2017.tolist()
total_2017 = total_2017[0]

provider_score = papers_2017/total_2017


