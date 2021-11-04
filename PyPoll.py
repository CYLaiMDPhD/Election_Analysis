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

# Initialize total_votes to 0
total_votes = 0

# Find all candidates
candidate_options = []
# Make empty dictionary to store votes for each candidate
candidate_votes = {}

# Open file and read it
with open(file_to_load) as election_data:
    # Read file as a csv using csv.reader function
    file_reader = csv.reader(election_data)

    # Read/skip the headers row
    headers = next(file_reader)

    # Set variables for winner
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Iterate through all rows
    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Get candidate name
        candidate_name = row[2]

        # Add candidate name to candidate options list if not in the list already
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Add candidate name to dictionary
            candidate_votes[candidate_name] = 0
       
        candidate_votes[candidate_name] += 1


# Find percentage of votes for each candidate
for candidate_name in candidate_votes:
    # Get votes for each candidate,  then calculate percent
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100
    print(f"{candidate_name}: {round(vote_percentage,1)}% ({votes:,})\n")

    # Determine winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Print results
winning_candidate_summary = (
    f"-------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------------------\n"
)
print(winning_candidate_summary)
