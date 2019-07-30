#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:25:09 2019

@author: ep9k
"""

"""Main module to show how we've been interpreting the 1figr data. Data
about UVA's big deal scholarly publication contracts. We are pulling from
JournalsPerProvider.csv"""


import JR1_functions as jr1
import JR5_functions as jr5
import other_functions_uva_big_deal as other
import vrl_presentation_functions as vrl
    

if __name__ == '__main__':
    
    
####FOR VRL meeting 8/5#####

    #Multiple Vendors
#    vrl.jr1_big5_jr80_jr90_jr95_stacked_bar()
#    vrl.jr5_big5_jr80_jr90_jr95_stacked_bar()
#    vrl.references_big5_jr80_jr90_jr95_stacked_bar()
#    vrl.papers_big5_jr80_jr90_jr95_stacked_bar()
#    vrl.big5_percent_jr5_of_jr1()
#    vrl.big5_cost_per_jr1_download()
#    vrl.big5_cost_per_jr5_download()
#    vrl.total_references_uva_authors()
#    vrl.uva_references_over_time()
#    vrl.number_of_articles_published_per_year()
#    vrl.number_uva_papers_over_time()
#    vrl.percent_uva_papers_over_time()     # has % formatting
#    vrl.oa_percent_papers_available_over_time() 

    
#    #Elsevier only
  
#    vrl.jr1_by_discipline_by_provider('Elsevier')
#    vrl.jr5_by_discipline_by_provider('Elsevier')
#    vrl.references_by_discipline_by_provider('Elsevier')
    vrl.papers_by_discipline_by_provider('Elsevier')
    
    
    

