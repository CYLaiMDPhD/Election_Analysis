# Data we need to retrieve:
# 1. Total number of votes cast.
# 2. Complete list of candidates who received votes.
# 3. Percentage of votes each candidate won.
# 4. Total number of votes each candidate won.
# 5. Winner of the election based on popular vote.

# Add Dependencies
import csv
import random
import numpy
import os


# Make variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Make object and path for output file
file_to_save = os.path.join("Analysis","election_analysis.txt")
#with open(file_to_save, "w") as txt_file:


# Open file and read it
with open(file_to_load) as election_data:
    # Read file as a csv using csv.reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
