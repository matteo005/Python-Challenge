import os
import csv

#Create all Lists needed
Months = []
Profits = []
Change = []

# Module for reading CSV files
csvpath = os.path.join('..', 'Resources', 'Budget_Data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Fill Lists with data
        Months.append(row[0])
        Profits.append(int(row[1]))

    #go through monthly profits
    for i in range(len(Profits)-1):

        #get the Monthly difference
        Change.append(Profits[i+1]-Profits[i])

#set Max and Min values
MaxIncrease = max(Change)
MaxDecrease = min(Change)

#Get Max and Min corresponding Months
MaxMonth = Change.index(max(Change)) +1
MinMonth = Change.index(min(Change)) +1

#get Average Sum
AvgChgSum = sum(Change)
#get Average Count
AvgChgLen = len(Change)
#Get Average Total
AvgerageChange = AvgChgSum/AvgChgLen


#Print all Results
print("\n")
print("            ""Financial Analysis")
print("----------------------------------------")
print(f"Total Months:  {len(Months)}")
print(f"Total: ${sum(Profits)}")
print(f"Average Change: {round((AvgerageChange),2)}")
print(f"Greatest Increase: {Months[MaxMonth]}  $({MaxIncrease})")
print(f"Greatest Increase: {Months[MinMonth]}  $({MaxDecrease})")
print("----------------------------------------")
print("\n")

    #Create PyBank.txt file
with open("PyBank.txt", "w") as file:

    # # Write all values
    file.write("            ""Financial Analysis")
    file.write("\n")
    file.write("----------------------------------------")
    file.write("\n")
    file.write(f"Total Months:  {len(Months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Profits)}")
    file.write("\n")
    file.write(f"Average Change: {round((AvgerageChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase: {Months[MaxMonth]}  $({MaxIncrease})")
    file.write("\n")
    file.write(f"Greatest Increase: {Months[MinMonth]}  $({MaxDecrease})")
    file.write("\n")
    file.write("----------------------------------------")