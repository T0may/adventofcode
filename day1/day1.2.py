#Day 1.2 adventofcode.com 2023
import re

input = open("day1/input.txt")
read = input.read()

replace_dict = {
    'one':'o1e',
    'two':'t2o',
    'three':'t3e',
    'four':'f4r',
    'five':'f5e',
    'six':'s6x',
    'seven':'s7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

calibrated_lines = read.strip().split('\n')


result_list = []

for line in calibrated_lines:
    for (key, value) in replace_dict.items():
        if key in line:
            line = line.replace(key, value)
    digits_only = re.sub(r'\D', '', line)
    first_digit = int(digits_only[0])
    last_digit = int(digits_only[-1])

    result = int(str(first_digit) + str(last_digit))
    result_list.append(result)

print(sum(result_list))