#PyBank # code riped from repo https://butler.bootcampcontent.com/Joel/homework/-/blob/5676aadd19a34e7d08de68b986c2e99140d47788/Python-Challenge/Solutions/PyBank/PyBank.py

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("c://","pythonstuff", "budget_data.csv")
file_to_output = os.path.join("c://","pythonstuff","budget_analysis.txt")

# Variable and list definition
total_months = 0
total_Prof = 0
month_of_change = []
Prof_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


# Read the csv and convert it into a list
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_Prof += int(first_row[1])
    prev_Prof = int(first_row[1])

    for row in reader:

        # Track the total ammount of month equal to row in data and calculate a subtotal of the Profit
        total_months +=  1
        total_Prof += int(row[1])

        # Track the profit changes
        Prof_change = int(row[1]) - prev_Prof
        prev_Prof = int(row[1])
        Prof_change_list += [Prof_change]
        month_of_change += [row[0]]

        # Compare greatest increase to the montly change and if it higher than the preivous value it store its date and ammount
        if Prof_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = Prof_change

        # Compare greatest decrease to the montly change and if it lower than the preivous value it store its date and ammount
        if Prof_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Prof_change

# Calculate the Average profit change
Prof_monthly_avg = round(sum(Prof_change_list) / len(Prof_change_list),2)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_Prof}\n"
    f"Average  Change: ${Prof_monthly_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
