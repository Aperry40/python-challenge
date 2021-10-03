import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
total_months = 0
net_changes = []
month_changes = []
months = []           #initialize the list of months
total_net_profit = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader) #header row
    firstrow = next(csvreader) #first row of dates, profits
    total_months = total_months + 1
    total_net_profit += int(firstrow [1])
    prev_net_profit = int(firstrow[1])
    for row in csvreader:
       total_months = total_months + 1
       total_net_profit += int(row[1])

       net_change = int(row[1]) - prev_net_profit
       net_changes.append(net_change)
       month_changes.append(row[0])
       prev_net_profit = int(row[1])

       months.append(row[0])            #add first month the change occured

avg_net_change = sum(net_changes)/len(net_changes)

greatestIncrease = [months[0], month_changes [0]]    
greatestDecrease = [months[0], month_changes [0]]
    
for m in range(len(month_changes)):
    if(month_changes[m] > greatestIncrease[1]):
        greatestIncrease[1] = month_changes[m]
        greatestIncrease[0] = months[m]   #update the month

    if(month_changes[m] < greatestDecrease[1]):
        greatestDecrease[1] = month_changes[m]
        greatestDecrease[0] = months[m]   #update the month


print(f"total months: {total_months}")    
print(f" Total: {total_net_profit}")
print(f"Average Change: ${avg_net_change:,.2f}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} Amount ${greatestIncrease[1]}")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} Amount ${greatestDecrease[1]}")