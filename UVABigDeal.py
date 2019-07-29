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

#    jr5.read_jr5()
#    jr5.read_jr5_no_elsevier()
#    jr5.jr5_big5()
#    jr5.jr5_other_providers()
#
#    jr1.read_jr1()
#    jr1.read_jr1_no_elsevier()
#    jr1.jr1_big5()
#    jr1.jr1_other_providers()
#
#    jr1.jr1_jr5_big5_grouped_bar_chart() 
#    jr1.jr1_jr5_other_providers_grouped_bar_chart()
#       
#    other.percent_jr5_of_jr1()
#    other.journals_by_domain()
#    other.journals_by_field()
#
#    other.journals_by_field_big5()
#    other.journals_by_field_other_providers()    
    
#    jr1.jr1_fluff_checker('Springer')
#    jr1.jr1_fluff_score()
#    jr1.jr1_big5_by_field('Engineering')
#    jr5.jr5_big5_by_field('Engineering') #(What e)

#    other.scopus_uva_publications_2017()    
#    other.scopus_uva_publications_all_years()
    
    
    
####FOR VRL meeting 8/5#####

    #Multiple Vendors
    vrl.jr1_big5_jr80_jr90_jr95_stacked_bar()
    vrl.big5_percent_jr5_of_jr1()
    vrl.big5_cost_per_jr1_download()
    vrl.big5_cost_per_jr5_download()
    
#    #Elsevier only
    
    vrl.uva_references_over_time('Elsevier')
    vrl.percent_uva_papers_over_time('Elsevier')
    vrl.oa_percent_papers_available_over_time('Elsevier')   
    vrl.jr1_by_discipline_by_provider('Elsevier')
    vrl.jr5_by_discipline_by_provider('Elsevier')
    vrl.references_by_discipline_by_provider('Elsevier')
    vrl.papers_by_discipline_by_provider('Elsevier')
    
    
    
    
    
    
#    vrl.big5_jr80_jr1_downloads()
#    vrl.big5_jr90_jr1_downloads()
#    vrl.big5_jr95_jr1_downloads()
#    vrl.big5_jr80_jr5_downloads()
#    vrl.big5_ref80_references()
#    vrl.big5_pap80_papers()  
#    vrl.number_uva_papers_over_time()
#    vrl.percent_uva_papers_over_time()

#    vrl.oa_percent_papers_available_over_time()
#    vrl.oa_number_papers_available_over_time()
#    vrl.number_oa_papers_by_discipline('Elsevier')
#    vrl.percentage_oa_papers_by_discipline('Elsevier')

