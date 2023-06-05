import csv, os

# CSV pile path
csv_file_path = os.path.join("Resources",'budget_data.csv')

#Text file path setup
txt_file_path = os.path.join("Analysis",'budget_analysis.txt')

#Read CSV file
with open(csv_file_path, 'r') as file:

    csv_reader = csv.reader(file)

    #Skip header
    next(csv_reader)

    #Establish variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    dates = []

    #Loop through rows in CSV file
    for row in csv_reader:
        date = row[0]
    
        profit_loss = int(row[1])

       #Calculate profit change from previous
        total_months += 1
        net_total += profit_loss
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        previous_profit_loss = profit_loss

   #Calculate average change
    average_change = sum(changes)/ len(changes)

    #Calculate maximum increase and decrease
    max_increase = max(changes)
    max_decrease = min(changes)

    max_increase_date = dates[changes.index(max_increase)]
    max_decrease_date = dates[changes.index(max_decrease)]

with open(txt_file_path, 'w') as txtfile:

    output = (
        f"Financial Analysis\n"
        f"-------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: $ {net_total} \n"
        f"Average Change: $ {round(average_change, 2)}\n"
        f"Greatest Increase in Profits: {max_increase_date} $ ({max_increase})\n"
        f"Greatest Decrease in Profits: {max_decrease_date} $ ({max_decrease})\n"
    )
  #Print results
    print(output)
    txtfile.write(output)