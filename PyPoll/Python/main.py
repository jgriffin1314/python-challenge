import os
import csv

csvpath = os.path.join('..', 'Resources', 'PyPoll.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

# Votes Cast
    # row_count = sum(1 for row in csvreader)
    # print(row_count)
    Voter_ID_List = []
    Voter_Count = 0
    Candidates = []
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Otooley_count = 0

    for row in csvreader:
        if row[0] not in Voter_ID_List:
            Voter_Count += 1
            Voter_ID_List.append(row[0])
        
        New_Candidate = row[2]
        if New_Candidate not in Candidates:
            Candidates.append(New_Candidate)

        if row[2] == "Khan":
            Khan_count = Khan_count + 1
        if row[2] == "Correy":
            Correy_count = Correy_count + 1
        if row[2] == "Li":
            Li_count = Li_count + 1
        if row[2] == "O'Tooley":
            Otooley_count = Otooley_count + 1
        

    khan_vote_percentage = round(Khan_count/Voter_Count*100,3)
    correy_vote_percentage = round(Correy_count/Voter_Count*100,3)
    li_vote_percentage = round(Li_count/Voter_Count*100,3)
    Otooley_vote_percentage = round(Otooley_count/Voter_Count*100,3)

    vote_percentages = [khan_vote_percentage, correy_vote_percentage, li_vote_percentage, Otooley_vote_percentage]

    dict = {Candidates[i]: vote_percentages[i] for i in range(len(Candidates))}

    max_value = max(dict, key=dict.get)

print(Voter_Count)
print(Candidates)
print("Khan won " + str(khan_vote_percentage) + '% of votes')
print("Correy won " + str(correy_vote_percentage) + '% of votes')
print("Li won " + str(li_vote_percentage) + '% of votes')
print("O'Tooley won " + str(Otooley_vote_percentage) + '% of votes')

print("Khan won " + str(Khan_count) + ' votes')
print("Correy won " + str(Correy_count) + ' votes')
print("Li won " + str(Li_count) + ' votes')
print("O'Tooley won " + str(Otooley_count) + ' votes')
print("The winner of the election is " + str(max_value))


# print(str(dict))
# print(max_value)
# print(Li_count)
# print(Voter_Count)
# print(Candidates)
# print(khan_vote_percentage)
# print(correy_vote_percentage)
    # import pandas as pd 
    # df = pd.read_csv(csvpath)
    # Candidates = []
    # Candidates = df["Candidate"].unique()
    # Vote_count = df["Candidate"].count()
    # print(Candidates)
    # print(Vote_count)

    #For candidate in Candidates:
     #   if candidate = row[3]:

   # Candidate_Count = -1
    # for row in csvreader:
    #     if row[2] not in Candidates:
    #         Candidate_Count += 1
    #         Candidates.append(row[2])
    # print(Candidate_Count)















# #Count Unique Months
#     Months = []
#     Profit_Loss_List = []
#     Months_count = -1
#     for row in csvreader:
#         if  row[0] not in Months:
#             Months_count += 1
#             Months.append(row[0])
#             print(Months_count)
#         Profit_Loss_Change = row[1] - Profit_Loss_List[-1]
#         Profit_Loss_List.append(row[1])
#         print(Profit_Loss_Change)