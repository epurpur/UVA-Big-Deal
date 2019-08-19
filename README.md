GitHub repository for 1Figr data

-Will Share Original with you (Google Docs or Box?)

JR1 - "Articles downloaded in 2017, but published in any year"
JR5 - "Articles dowloaded in 2017 and published in 2017" (Current articles)

-JournalsPerProvider is what we are working from (JournalsPerProvider.csv)
  - make sure you perserve the .csv format (CSV UTF-8 comma delimited)
  - I've formatted all the numerical columns I've been working with as numbers
  
-Python Packages used (mostly):
  -pandas: for parsing the csv file
  -matplotlib: for making charts
  
-Different files in the "UVA Big Deal" repository
  -UVABigDeal.py - the file I run all the functions from. Imports functions from other files
  -vrl_presentation_functions.py - this file contains all the functions I used to create visuals for the VRL (Virginia         
                                   Research Libraries) August 5th meeting. These are the ones we want to clean up first!
                                   
  -JR1_functions.py - Handles only JR1 related functions
  -JR5_funtions.py - Handles only JR5 related functions
  -other_functions_uva_big_deal.py - Other functions that don't neatly use JR1 or JR5 data
  
  -weekly updates, for our internal use. You can look if you want. They may not make much sense because the project has     
  evolved.
  
  We can use these as help but probably not worth cleaning up


To Do List:
-Familiarize yourself with the existing code
-Make nice, consistent Documentation strings for the vrl_presentation_functions. I'd like them to be consistent as most of 
them are similar data sliced and diced different ways.
-Descriptive variable names (as best we can)
-more documentation in code if needed (using #)
-Add labels to a couple of the plots (jr80_jr90_jr95 functions)
-fix the "JournalsPerProvider_noJR1" and "JournalsPerProvider_noJR5" null values

Later:
-Migrate project to GitLab?

  
  
