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
    #fetching the candidates in ascending alphabetical order and storing them in cand_list
    cand_list = list(set(candidate))
    cand_list.sort()
    #print(cand_list)
    #cand_list = []
    votes_per_cand = []
    for x in cand_list:
        vote = votes_per_cand.append(candidate.count(x))
        #print(x)
        
    for c in range(len(cand_list)):
        print(f"{cand_list[c]}: {'{:.2%} '.format(votes_per_cand[c]/len(candidate))}({votes_per_cand[c]})")
    
    print(f"Winner: {cand_list[votes_per_cand.index(max(votes_per_cand))]}")

  #  for x in cand:
  #  if x not in output:
  #      output.append(x)
  #      print(output)

print("Election Results")
print("-" * 100 )
print(f"Total Votes: {len(voters)}")
print("-" * 100 )
print(f"Winner: {cand_list[votes_per_cand.index(max(votes_per_cand))]}")

file = open("output.txt","w")
file.write("Election Results" + "\n")
file.write("-" * 100 + "\n")
file.write((f"Total Votes: {len(voters)}") + "\n")
file.write("-" * 100 + "\n")
file.close()


