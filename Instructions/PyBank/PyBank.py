# importing libraries
import os
import csv
import sys

# referencing input csv
csvpath = os.path.join('Resources','budget_data.csv')
print(csvpath)

# opening and reading csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
   
    total = []
    average_change = []
    next(csvreader)  # skip the headers
    profits = []
    
    #read through each row of data after header
    for rows in csvreader:
        profits.append(int(rows[1]))
        total.append(rows[0])

    # Compute average change
    for rows in range(1, len(profits)):
        average_change.append((int(profits[rows]) - int(profits[rows-1])))
    
    total_months = len(total)                                   # to find out the number of months
    average_revenue = sum(average_change) / len(average_change) # average of change in profit/losses over entire period 
    greatest_increase = max(average_change)                     # greatest increase in profit by months
    greatest_decrease = min(average_change)                     # greatest decrease in profit by months
    greatest_month_index = total[average_change.index(max(average_change))+1]
    lowest_month_index = total[average_change.index(min(average_change))+1]

    # print Results in terminal
    print("Financial Analysis")
    print("-" * 100)
    print("Total Months: ", total_months)
    print("Total: $", sum(profits))
    print("Average change: $", round(average_revenue, 2))
    print(f"Greatest Increase in Profits: ", str(greatest_month_index) + \
        "($ " + str(greatest_increase) + ")")
    print(f"Greatest Decrease in Profits: ", str(lowest_month_index) + \
        "($ " + str(greatest_decrease) + ")")

    # new text file output to a text file

    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("-" * 100 + "\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(profits)) + "\n")
    file.write("Average change: " + "$" + str(round(average_revenue, 2)) + "\n")
    file.write("Greatest Increase in Profits: " + str(total[average_change.index(max(average_change))+1]) + " " + "($" + str(greatest_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(total[average_change.index(min(average_change))+1]) + " " + "($" + str(greatest_decrease) + ")" + "\n")
    file.close()
