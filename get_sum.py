#lesson 2 assignment for Using Python to Access Web Data
#import regex lib
import re
#get the data file
sum_data = open('regex_sum_196353.txt')
#create list for numbers
num_list = list()
#run loop to find numbers and append to output
for line in sum_data:
    num = re.findall('([0-9]+)', line)
    for pos in num:
        add_num = float(pos)
        num_list.append(add_num)
#print output
print sum(num_list)
