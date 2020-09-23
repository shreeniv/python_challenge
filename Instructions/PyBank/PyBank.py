import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')
print(csvpath)

"""
# we need the total number of months - first row is the hearder
 - so one less than the number of months;
# also need to keep track of the total 
- running total of the profit and loss
# avg change is similar to yearly change in vba hw
 - keep track by using variables - grab certain information as
  we read thru the file
# Avg Change = value in the very last row minus the value
 in the very first row divided by changes in number of months
# running total of greatest increase and greatest 
decrease  - using dictionary
# need to add debugging statements
# python grading rubric - code should be clean and committed
 - should show progress of commits and saving on git
"""

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
   
    count = 0
    total = 0
    profits = []
    next(csvreader)  # skip the headers
    for row in csvreader:
        count = count + 1
        total = total + eval(row[1])
        profits.append(eval(row[1])) 
    
    profits.sort()
    print("Total Number of Months: ", count)
    print("Total : ", total)
    print("Greatest Increase in Profits: ", profits[-1])
    print("Greatest Decrease in Profits: ", profits[0])
