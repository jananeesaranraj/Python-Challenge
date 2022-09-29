import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")
date=[]
revenue=[]
revenue_change = []

# rowcount = 0
# total = 0
# change = 0
# greatest_increase = 0

# def print_analysis(data):
#     date = str(data[0])
#     revenue= int(data[1])
#     global total
#     total += revenue
#     global change
#     global greatest_increase
#     if revenue > 0:
#         change = change + revenue
#         if change > greatest_increase:
#               greatest_increase = change

with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        date.append(row[0])
        revenue.append (float(row[1]))   
        #rowcount += 1
        #print_analysis(row)
    for i in range(1,len(revenue)):
        revenue_change.append(revenue[i] - (revenue[i-1]))
        avr_rev_change = sum(revenue_change)/len(revenue_change)

        greatest_increase = max(revenue_change)
        greatest_decrease = min(revenue_change)
        
        greatest_increase_date =str(date[revenue_change.index(greatest_increase)])
        greatest_decrease_date = str(date[revenue_change.index(greatest_decrease)])

print("Finalcial Analysis")
print("----------------------------------------------------------------")
print("Total Months: " + str(len(date)))
print("Total : $" + str(sum(revenue)))
print("Average Change: $" + str(avr_rev_change))
print("Greatest Increase in Profits:"+ str(greatest_increase_date) + "$(" + str(greatest_increase)+ ")")
print("Greatest Decrease in Profits:"+ str(greatest_decrease_date) + "$("+ str(greatest_decrease)+ ")")

output_file = os.path.join("Analysis","bank.txt")

with open(output_file,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("-------------------------------------------\n")
    text.write("Total Months: " + str(len(date)) + "\n")
    text.write("Total : $"+ str(sum(revenue)) + "\n")
    text.write("Average Change: $" + str(avr_rev_change) + "\n")
    text.write("Greatest Increase in Profits:"+ str(greatest_increase_date) + "$("+str(greatest_increase) +")" + "\n")
    text.write("Greatest Decrease in Profits:"+ str(greatest_decrease_date) + "$("+str(greatest_decrease )+")" + "\n")
    


