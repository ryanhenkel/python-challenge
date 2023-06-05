import csv, os

# CSV pile path
csv_file_path = os.path.join("Resources",'election_data.csv')

#Text file path setup
txt_file_path = os.path.join("Analysis",'election_analysis.txt')

# Establish variables
total_votes = 0
candidates = {}
winner_votes = 0
winner = " "

# Open CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        #Count total votes
        total_votes += 1

        #Grab candidates name
        candidate = row[2]

        #Add candidate
        if candidate not in candidates:
            candidates[candidate] = 0

        #Count candidate's votes
        candidates[candidate] += 1

with open(txt_file_path, 'w') as txtfile:

    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"

    )
    #Print results
    print(output)
    txtfile.write(output)

    #Calculate percentage of votes & print
    for candidate, votes in candidates.items():
        percent = (votes / total_votes) * 100
        print(f"{candidate}: {percent:.3f}% ({votes})")
        txtfile.write(f"{candidate}: {percent:.3f}% ({votes})\n")

        #Count who has the most votes
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate

    output = (
        f"-------------------\n"
        f"Winner: {winner}\n"
        f"--------------------\n"
    )
    #Print results
    print(output)
    txtfile.write(output)