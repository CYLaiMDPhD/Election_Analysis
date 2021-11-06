# Election_Analysis

*Note: This repository was generated to fulfill assignments (Module 3 Exercises and Challenge) for the UC Berkeley Data Analytics and Visualization Bootcamp. Challenge submitted on 11-6-21 for grading.*

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


### Resources

* Data Source: election_results.csv
* Software: Python 3.8.8, Visual Studio Code 1.61.2


### Summary

The Analysis of the election show that:

* There were 369,711 votes cast in the election.
* The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

* The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

* The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.


---

## Challenge Overview
This challenge builds off of previous work we performed for the Colorado Board of Elections to include additional vote results by county. 


## Challenge Summary and Results

### Overview of Election Audit
In addition to our previous audit of election results by candidate, the election commission has requested information about voting results by county. This supplemental analysis adds county vote results (total votes per county, percentage of votes per county, and county with largest voter turnout) for this election.

The same source material and software was used for this additional analysis was the same as those used for the above preliminary summary ("election_results.csv", Python 3.8.8, and Visual Studio Code 1.61.2). The full audit results are presented below.

### Election Audit Results
A total of 369,711 votes were cast for this election across three counties. Unfortunately, we do not have the total number of registered voters across these three counties to determine absolute voter turnout.

#### Results by Candidate:
* Of the three candidates in this election, Diana DeGette won by a landslide, having received 73.% of the votes. Raymon Anthony Doane received the least number and percentage of votes. The percentage and all votes received for each candidate are:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

#### Results by County:
* Of the three counties from which votes were cast for this election, voters in Denver county cast the most votes. Nearly 83% of all votes cast originated from Denver county. The percentage and total number of votes by county are summarized below:
  - Jefferson county: 10.5% and 38,855 total votes
  - Denver county: 82.8% and 306,055 total votes
  - Arapahoe county: 6.7% and 24,801 total votes

### Election Audit Summary
This election audit was carried out using a relatively straightforward python script. This script may be used for future elections with different candidates and other regional elections if results are provided in the same csv format. The script was written such that the number of candidates and counties may change depending on the election results file by using variables and python lists and dictionaries. The only code that needs modification for other election results are those referencing the path and results file used and output files (i.e. "2021_special_election_results.csv" instead of "election_results.csv"). The script may also be modified in the future to run multiple audits by looping through a list of election results. Additional analysis that could be included in the future is a breakdown of number of votes by both county and candidate, which may provide insight into each county's support for a particular candidate. In this particular election, with Denver county contributing to over 80% of all votes cast and the winner receiving over 70% of the vote, Denver county clearly had more influence over other counties, but we don't know what percentage of Denver county voters supported the winner. 


