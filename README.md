GitHub repository for 1Figr data


Steps to use data...

1- Save the 'JournalsPerProvider' tab from your master copy of the 1Figr/1Science Dataset as CSV file as 'JournalsPerProvider.csv'.  Must be in 
UTF-8 encoding to be read correctly by Pandas.

2- Notice in the 'JournalsPerProvider' CSV document that the column headers begin on row 8. Keep it this way. The code 
skips to the 8th row, and then begins parsing the data.

*Probably the easiest way to do steps 3-7 is in Microsoft Excel. 

3- Open the CSV document (JournalsPerProvider.csv) in excel and 
format the data in the following columns as 'numeric' data type. If you don't do this, Pandas reads these as strings or some 
other undefined data type:
'Downloads JR1 2017', 'Downloads JR5 2017 in 2017', 'References', 'Papers' (These should be columns H,I,J,K in your dataset).

4- Rename the following columns under 'Papers per journal/provider by your institution's authors (As Measured in Scopus)' 
(should be columns AA - AJ) as 'papers_2008', 'papers_2009', 'papers_2010' and so on. Then change the data in all these 
columns to 'numeric' data type.

5- Repeat the process for all columns under 'References to journal/provider by your institution's authors (As measures in 
Scopus)' (should be columnns AK-AT) as 'ref_2008', 'ref_2009', 'ref_2010' and so on. Change data in these columns to 
'numeric' data type.

6- Repeat the process for all columns under 'OA papers in 1findr per journal/provider (Intersection with Scopus)' (should be 
columns AU-BD) as 'oa_papers_2008', 'oa_papers_2009', 'oa_papers_2010' and so on. Change data in these columns to 'numeric' 
data type.

7- Repeat the process for all columns under 'Total Papers in Scopus per journal/provider' (should be columns BO-BX) as 
'total_2008', 'total_2009', 'total_2010'. Change data in these columns to 'numeric' data type.

8- Lastly, keep in mind your 'JournalsPerProvider.csv' file should be saved in the working directory or same directory as the 
code. Otherwise you'll have to change the file paths at the beginning of each function to read to the new working directory. 








~~~~~~~~~
To Do list
~~~~~~~~~
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
-Familiarize yourself with the existing code, JournalsPerProvider.csv data
-Make nice, consistent Documentation strings for the vrl_presentation_functions. I'd like them to be consistent as most of 
them are similar data sliced and diced different ways. Uniform documentation strings.
-Descriptive variable names (as best we can). Uniform variable names.
-more documentation in code if needed (using #)

-Add labels to a couple of the plots (jr80_jr90_jr95 functions)


Later:
-Migrate project to GitLab?

  
  
