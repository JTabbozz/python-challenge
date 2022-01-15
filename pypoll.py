# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("c://","pythonstuff", "election_data.csv")
file_to_output = os.path.join("c://","pythonstuff","election_analysis.txt")

# Variable and list definition
total_number_of_votes=0
candidates_list=[]
Results=[]
candi_results_dic={}

# Read the csv and convert it into a list
with open(file_to_load) as poll_data:
    reader = csv.reader(poll_data)

# Read the header row
    header = next(reader)

# Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_number_of_votes+=1

    for row in reader:
        row = next(reader)
        Results.append(row)
        total_number_of_votes+=1
        
        #compile unique candidate list 
        candi_name=row[2]
        
        if candi_name not in candidates_list:
            candidates_list.append(candi_name)
            candi_results_dic[candi_name]=0
        
        #equivalent to else
        candi_results_dic[candi_name]+=1




#Find the key associated to max value https://tutorialdeep.com/knowhow/key-maximum-value-dictionary-python/ 
MaxDictVal = max(candi_results_dic, key=candi_results_dic.get)

#print candidates using the key and specified candidate 
keys=candi_results_dic.keys()
values=candi_results_dic.values()

candi_1_perc=(round(candi_results_dic["Khan"]/total_number_of_votes*100,2))
candi_1_votes=(candi_results_dic["Khan"])

candi_2_perc=(round(candi_results_dic["Correy"]/total_number_of_votes*100,2))
candi_2_votes=(candi_results_dic["Correy"])

candi_3_perc=(round(candi_results_dic["Li"]/total_number_of_votes*100,2))
candi_3_votes=(candi_results_dic["Li"])

candi_4_perc=(round(candi_results_dic["O'Tooley"]/total_number_of_votes*100,2))
candi_4_votes=(candi_results_dic["O'Tooley"])

output=(
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_number_of_votes}\n"
    f"-------------------------\n"
    f"\n"
    f"Khan: {candi_1_perc} % ({candi_1_votes})\n"
    f"Correy: {candi_2_perc} % ({candi_2_votes})\n"
    f"Li: {candi_3_perc} % ({candi_3_votes})\n"
    f"O'Tooley: {candi_4_perc} % ({candi_4_votes})\n"
    f"------------------------\n"
    f"Winner: {MaxDictVal}")

# Checks if all votes are assigned to the candidates
total_four_votes=(candi_1_votes+candi_2_votes+candi_3_votes+candi_4_votes)
if (total_four_votes)<total_number_of_votes:
    print(f"Warning - {total_number_of_votes-total_four_votes} votes outside the nominated list")
# Print the output (to terminal)

print(output)

# Export the results to text file
with open(file_to_output, "w") as f:
    f.write(output)