# PyBank Assignment
# Author : Milinda 'ML' Liyanage
# Date : 2021-05-26

import os
import csv
import string

csv_in_path = os.path.join('Resources','PyBank_budget_data.csv')
txt_out_path = os.path.join('analysis','PyBank_analysis.txt')

# Define and initialise variables
total_pl = 0.00
current_pl = 0.00
previous_pl = 0.00
total_diff_pl = 0.00
diff_pl = 0.00
max_diff_pl = 0.00
min_diff_pl = 0.00

with open(csv_in_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    counter = 0

    # while the fle is open all referance to it must be indented
    for row in csvreader:
        counter += 1
        total_pl = total_pl + int(row[1])

        current_pl = int(row[1])

        # skip the first data row when calculating the differance from previous month
        if counter > 1:
            diff_pl = current_pl - previous_pl
            total_diff_pl = total_diff_pl + diff_pl

            if max_diff_pl < diff_pl:
                max_diff_pl = diff_pl
                max_diff_month = row[0]

            if min_diff_pl > diff_pl:
                min_diff_pl = diff_pl
                min_diff_month = row[0]

        # save the current value, which is required for the calc in the record
        previous_pl = current_pl

# format the output
no_months_str =  str(counter)
total_pl_str = '${0}'.format(format(total_pl, ',.0f'))
average_change_str = '${0}'.format(format(total_diff_pl/(counter-1), ',.2f'))
max_diff_pl_str = '(' + '${0}'.format(format(max_diff_pl, ',.0f')) + ')'
min_diff_pl_str = '(' + '${0}'.format(format(min_diff_pl, ',.0f')) + ')'

# print the output to the screen
print('Financial Analysis')
print('----------------------------------------------------')
print('Total Months: ' + no_months_str)
print('Total: ' + total_pl_str )
print('Average Change: ' + average_change_str )
print('Greatest Increase in Profits: ' + max_diff_month + ' ' + max_diff_pl_str)
print('Greatest Decrease in Profits: ' + min_diff_month + ' ' + min_diff_pl_str)

# write the results to a text file
with open(txt_out_path, 'w')  as txtfile:

    print('Financial Analysis', file=txtfile)
    print('----------------------------------------------------',  file=txtfile)
    print('Total Months: ' + no_months_str,  file=txtfile)
    print('Total: ' + total_pl_str,  file=txtfile)
    print('Average Change: ' + average_change_str,  file=txtfile )
    print('Greatest Increase in Profits: ' + max_diff_month + ' ' + max_diff_pl_str ,  file=txtfile)
    print('Greatest Decrease in Profits: ' + min_diff_month + ' ' + min_diff_pl_str ,  file=txtfile)

