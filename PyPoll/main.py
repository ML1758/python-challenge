# PyPoll Assignment
# Author : Milinda 'ML' Liyanage
# Date : 2021-05-26

import os
import csv
import string

csv_in_path = os.path.join('Resources','PyPoll_election_data.csv')
txt_out_path = os.path.join('analysis','PyPoll_analysis.txt')

# Define and initialise variables
total_votes = 0
candidate_dict = {}

with open(csv_in_path) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)

        # while the fle is open all referance it must be indented
        for row in csvreader:

            total_votes +=1

            current_candidate = row[2]

            # skip the first data row when calculating the differance from prevous month
            if current_candidate in candidate_dict:
                # get current running total for candidate, increase by and store back
                x = candidate_dict.get(current_candidate) + 1
                candidate_dict[current_candidate] = x
            else:
                # if it is new candidate store new value in dictionary with a 1
                candidate_dict[current_candidate] = 1

# Sort the dictionary in reverse order of votes[1] and store in a list
candidate_sorted_list = (sorted(candidate_dict.items(), key=lambda x: x[1], reverse=True))

# format total votes to a string
total_votes_str = format(total_votes, ',.0f')

# write the results to a text file and to screen
with open(txt_out_path, 'w')  as txtfile:

    # write output to file
    print("Election Results", file=txtfile)
    print("---------------------------", file=txtfile)
    print("Total Votes: " + total_votes_str,  file=txtfile)
    print("---------------------------", file=txtfile)

    # print the output to the terminal
    print("Election Results")
    print("---------------------------")
    print("Total Votes: " + total_votes_str)
    print("---------------------------")

    # loop through the list
    for x, y, in candidate_sorted_list:
        candidate_name = x + ':'
        candidate_percentage_str = format((y/total_votes)*100, ',.3f') + '%'
        candidate_votes_str = '(' + format(y, ',.0f') + ')'

        #print to file
        print(candidate_name + ' ' + candidate_percentage_str + ' ' + candidate_votes_str , file=txtfile)
        #print to screen
        print(candidate_name + ' ' + candidate_percentage_str + ' ' + candidate_votes_str)

    # winner is the first row in the list
    winner = str(candidate_sorted_list[0])
    winner_name = winner[2:winner.find(',')-1]

    #print to file
    print("---------------------------", file=txtfile)
    print("Winner: " + winner_name, file=txtfile)
    print("---------------------------", file=txtfile)

    #print to screen
    print("---------------------------")
    print("Winner: " + winner_name)
    print("---------------------------")
