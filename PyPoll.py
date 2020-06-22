#  The data we need to retrieve.
#  1. The total number of votes cast
#  2. A complete list of candidates who received votes
#  3. The percentage of votes each candidate won
#  4. The total number of votes each candidate won
#  5. The winner of the election based on popular vote.

# dependants
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initial vote counter
total_votes = 0
# pulling candidate options
candidate_options = []
# declare empty dictonary
candidate_votes = {}
# winner candi and count and %
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open and read file
with open(file_to_load) as election_data:
        # to do : read and perform analysis  
        file_reader = csv.reader(election_data)
        
        # Read and print header row
        headers = next(file_reader)

        # print each row in the CSV file
        for row in file_reader:
                # add to total vote count
                total_votes += 1
                # print candidate name from each row
                candidate_name = row[2]
                
                if candidate_name not in candidate_options:
                        # add candidate name to list if no match exists
                        candidate_options.append(candidate_name)

                        # begin candidate vote tracking
                        candidate_votes[candidate_name] = 0
                # add vote to candi counb
                candidate_votes[candidate_name] += 1
# saving results to txt file
with open(file_to_save, "w") as txt_file:
# print the final vote count
         election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"-------------------------\n")
         print(election_results, end="")
        #save the final vote count to txt file.
         txt_file.write(election_results)
        # determine the % of votes for candies by looping thru count
         for candidate in candidate_votes:
                # retrieve vote count of a candi
                votes = candidate_votes[candidate]
                vote_percentage = float(votes) / float(total_votes) * 100
                # candi name and % + calc of percentage
                candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results)
                # #save to txt file
                txt_file.write(candidate_results)

                # Determine winning vote count and candi
                # Determine if the votes are greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        # If true then set winning_count = votes and winning_percent = vote_percentage.
                        winning_count = votes
                        winning_percentage = vote_percentage
                        # Set the winning_candidate equal to the candidate's name.
                        winning_candidate = candidate 
                                
         winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
         #print winner candi,  vote, %
         print(winning_candidate_summary)
         # save to txt
         txt_file.write(winning_candidate_summary)

                        