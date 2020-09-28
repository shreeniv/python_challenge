# importing dependent libraries
import os
import csv

# referencing input csv
csvpath = os.path.join('Resources','election_data.csv')
#print(csvpath)
# opening and reading csv
cand_list = []
votes_per_cand = []
candidate = []
voters = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    next(csvreader) # skip the headers

    # fetch the total number of candidate voted for to a list; to output length of that list and assigned to voters
    for row in csvreader:
        voters.append(row[0])
        candidate.append(row[2])
   
    # printing the values fpr Total number of votes
    print("Election Results")
    print("-" * 100 )
    print(f"Total Votes: {len(voters)}")
    print("-" * 100 )
    
    # list of commands for writing to output text file
    file = open("Analysis\output.txt","w")
    file.write("Election Results" + "\n")
    file.write("-" * 100 + "\n")
    file.write((f"Total Votes: {len(voters)}") + "\n")
    file.write("-" * 100 + "\n")

    #fetching the candidates in ascending alphabetical order and storing them in cand_list
    cand_list = list(set(candidate))
    cand_list.sort()
    #print(cand_list)
    #cand_list = []
    votes_per_cand = []
    for x in cand_list:
        vote = votes_per_cand.append(candidate.count(x))
        #print(x)

    # loop to fetch the percentage of votes each candidate won and to calculate total number of votes for them    
    for c in range(len(cand_list)):
        print(f"{cand_list[c]}: {'{:.2%} '.format(votes_per_cand[c]/len(candidate))}({votes_per_cand[c]})")
        file.write((f"{cand_list[c]}: {'{:.2%} '.format(votes_per_cand[c]/len(candidate))}({votes_per_cand[c]})") + "\n")

    # printing winner of the election based on popular vote   
    print("-" * 100 )
    print(f"Winner: {cand_list[votes_per_cand.index(max(votes_per_cand))]}")
    print("-" * 100 )
    
    # writing winner to the file
    file.write("-" * 100 + "\n")
    file.write((f"Winner: {cand_list[votes_per_cand.index(max(votes_per_cand))]}") + "\n")
    file.write("-" * 100 + "\n")
    file.close()