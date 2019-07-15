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
    

provider_name = 'Springer'                    #Changes output for the 'dependent' functions


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
#    
#    
#    ###### DEPENDENT FUNCTIONS - dependent on provider_name ############
#    jr5.jr5_by_field_by_provider(provider_name)
#    jr1.jr1_by_field_by_provider(provider_name)
#    other.references_by_field_by_provider(provider_name)
#    other.publications_by_field_by_provider(provider_name)
#    jr5.jr5_percent_field_by_provider(provider_name)
#    jr1.jr1_percent_field_by_provider(provider_name)
    
    
#    jr1.jr1_fluff_checker('Springer')
#    jr1.jr1_fluff_score()
#    jr1.jr1_big5_by_field('Engineering')
#    jr5.jr5_big5_by_field('Engineering') #(What e)

#    other.scopus_uva_publications_2017()    
#    other.scopus_uva_publications_all_years()
    
    
    
####FOR GROUP PRESENTATION 7/16#####
    
    jr1.jr1_fluff_score()               #change name of function!
    jr1.jr1_fluff_score_inverse()       #change name of function!  Contains list of provider w/ JR80 numbers
    other.percent_jr5_of_jr1()
    jr5.jr5_by_field_by_provider('Springer')
    jr5.jr5_by_field_by_provider('Sage')
    jr5.jr5_by_field_by_provider('Elsevier')
    jr5.jr5_by_field_by_provider('Wiley')
    jr5.jr5_by_field_by_provider('Taylor & Francis')
    other.scopus_uva_publications_2017()
    

