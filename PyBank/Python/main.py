import os
import csv

csvpath = os.path.join('..', 'Resources', 'PyBankresource.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

#Count Unique Months
    Months = [0,0]
    Profit_Loss_List = [867884]
    Profit_Loss_Change = 0
    Profit_Loss_Change_List = [0,0]
    Months_count = 0
    for row in csvreader:
        if  row[0] not in Months:
            Months_count += 1
            Months.append(row[0])
        Profit_Loss_List.append(row[1])
        Profit_Loss_Change = (int(Profit_Loss_List[-1]) - int(Profit_Loss_List[-2])) 
        Profit_Loss_Change_List.append(Profit_Loss_Change)

    Greatest_PL_Increase = max(Profit_Loss_Change_List)
    Increase_Index = Profit_Loss_Change_List.index(Greatest_PL_Increase)
    Greatest_PL_Increase_Month = Months[Increase_Index]

    Greatest_PL_Decrease = min(Profit_Loss_Change_List)
    Decrease_Index = Profit_Loss_Change_List.index(Greatest_PL_Decrease)
    Greatest_PL_Decrease_Month = Months[Decrease_Index]

    Average_PL_Change = (sum(Profit_Loss_Change_List)) / (Months_count-1)
    Average_PL_Change = round(Average_PL_Change,2)

    print("Total Months: " + str(Months_count))

# Sum Profit and Loss
    import pandas as pd 
    df = pd.read_csv(csvpath)
    Sum_P_L = df["Profit/Losses"].sum()


## Prints
    print("Total: $" + str(Sum_P_L))
    print("Average Change: $" + str(Average_PL_Change))
    print(Greatest_PL_Increase_Month + " ($" + str(Greatest_PL_Increase) + ")")
    print(Greatest_PL_Decrease_Month + " ($" + str(Greatest_PL_Decrease) + ")")
