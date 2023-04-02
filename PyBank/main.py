import csv
import os
import sys

months = []
income = 0
change = 0
monthly_income = []
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
#open csv file and store header
budget_data_csv = os.path.join("..", "Starter_Code", "PyBank", "Resources", "budget_data.csv" )
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    for row in csv_reader:
        #print(row[0])
        months.append(row[0])
        income += int(row[1])
        monthly_income.append(row[1])
    #print(months)
    


    for i in range(1, len(monthly_income)):
        net_change =  int(monthly_income[i]) - int(monthly_income[i-1])
        monthly_change.append(net_change)
        #print(change)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = months[i]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = months[i]
            greatest_decrease[1] = net_change
        Avg_monthly_change = sum(monthly_change) / len(monthly_change)
    
    
    # greatest_profit = max(monthly_change)
    # greatest_loss = min(monthly_change)
    
   
  
        
   #Results output function
    def print_output():
        print("Financial Analysis")
        print("---------------------------------")
        print("Total Months: " + str(len(months)))  
        print("Total: $" + str(income))
        print("Average Change: $" + str(Avg_monthly_change))
        print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
        print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
        
    #print(str(len(monthly_change)))

     #code function taken from howtodoinjava.com
    original_stdout = sys.stdout
    with open("analysis/Financial_Analysis.text", 'w') as f:
        sys.stdout = f
        print_output()
        sys.stdout= original_stdout
    
    print_output()


    # print(str(greatest_increase[0]))
    # print(str(greatest_increase[1]))

    # print(str(months))