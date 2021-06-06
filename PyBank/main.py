import os
import csv

budget_csv = os.path.join("Resources","PyBank_budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader,None)
    max_row = 0
    total_a = 0
    revenue = []
    date = []
    ave_rev = []
    #figure out the total row number
    for row in csvreader:
        if row[0] is not None:
            revenue.append(float(row[1]))
            date.append(row[0])
            max_row += 1
            total_a = total_a + int(row[1])

    for i in range(1,max_row):
        ave_rev.append(revenue[i] - revenue[i-1])
        arc = sum(ave_rev)/len(ave_rev)
   
        max_rev = max(ave_rev)
        min_rev = min(ave_rev)
        max_date = date[ave_rev.index(max_rev)+1]
        min_date = date[ave_rev.index(min_rev)+1]
    
    
  
    print("Financial Analysis\n")
    print("-------------------------------\n")
    print("Total Months: " + str(max_row)+"\n")
    print("Total: $" + str(total_a)+"\n")
    print("Average Change: $" + "%.2f" % arc+"\n")
    print("Greatest Increase in Revenue: " + str(max_date) + " ($" + "%.0f" % max_rev + ")\n")
    print("Greatest Decrease in Revenue: " + str(min_date) + " ($" + "%.0f" % min_rev + ")\n")

    file = open("Analysis/Pybank.txt","w")
    file.write("Financial Analysis\n")
    file.write("-------------------------------\n")
    file.write("Total Months: " + str(max_row)+"\n")
    file.write("Total: $" + str(total_a)+"\n")
    file.write("Average Change: $" + "%.2f" % arc+"\n")
    file.write("Greatest Increase in Revenue: " + str(max_date) + " ($" + "%.0f" % max_rev + ")\n")
    file.write("Greatest Decrease in Revenue: " + str(min_date) + " ($" + "%.0f" % min_rev + ")\n")
    file.close()