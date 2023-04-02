import csv
import os
import sys
total_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
vote_count = 0



election_data_csv = os.path.join("..", "Starter_Code", "PyPoll", "Resources", "election_data.csv")
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    

#build dictionary with candidate names and votes via compare
    for row in csv_reader:
        total_votes += 1
        name = row[2]
        if name in candidate_votes:
            candidate_votes[name] += 1
        else:
            candidate_votes[name] = 1
            candidate_list.append(name)

#determine winner - referenced code from https://datagy.io/python-get-dictionary-key-with-max-value/
winner = max(candidate_votes, key=candidate_votes.get)

#determine percentages and total vote counts by canddate and save as variables for output
pct_0 = round((candidate_votes[candidate_list[0]]/total_votes) * 100, 3)
pct_1 = round((candidate_votes[candidate_list[1]]/total_votes) * 100, 3)
pct_2 = round((candidate_votes[candidate_list[2]]/total_votes) * 100, 3)
votes_0 = candidate_votes.get(str(candidate_list[0]))
votes_1 = candidate_votes.get(str(candidate_list[1]))
votes_2 = candidate_votes.get(str(candidate_list[2]))

#output function

def print_output():
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"{candidate_list[0]} {pct_0}% ({votes_0})")
    print(f"{candidate_list[1]} {pct_1}% ({votes_1})")
    print(f"{candidate_list[2]} {pct_2}% ({votes_2})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")


#print output to file
original_stdout = sys.stdout
with open("analysis/Election_Analysis.text", 'w') as f:
        sys.stdout = f
        print_output()
        sys.stdout= original_stdout

print_output()








