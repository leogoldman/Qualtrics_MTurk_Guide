# Qualtrics_MTurk_Guide

This repository is intended to be a guide for researchers using MTurk, and specifically for those using MTurk to run Qualtrics surveys. A large part of the repository right now (Feb 2020) is geared towards helping researchers pay out bonuses in bulk in MTurk, which is not a streamlined process in the MTurk user interface.

# Included Files:
Qualtrics_MTurk_Bonus_Processing_Template.Rmd
  - This is an R markdown file that serves as a general template for processing Qualtrics results along with MTurk results to 
    create a file with Amazon Web Services (AWS) commmands to run at one time in a bash script.
  - This file is not intended to be run without editing. Each survey has its own attention checks and bonus payment scheme,   
    and the code will need to be edited to accomodate that.
    
Creating_Mturk_Account
  - This is a guide for getting started as a requester in MTurk
  
Paying MTurk Bulk Bonuses
  - This is a guide for paying bulk bonuses with minimal (although still some coding)
  
Using Bash to Efficiently Pay MTurk Bulk Bonuses
  - This is a more advanced guide to pay bulk bonuses. The process is streamlined and less prone to error than the simpler 
    guide, although it does require a fair amount of code (detailed steps included)
    
Qualtrics_MTurk_Tutorial
  - This is the slide deck from a Qualtrics/MTurk tutorial presentation given in Nov. 2019
