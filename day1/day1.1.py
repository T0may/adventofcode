#Day 1.1 adventofcode.com 2023
import re

input = open("day1/input.txt")
read = input.read()

calibrated_lines = read.strip().split('\n')
result_list = []

for line in calibrated_lines:
    digits_only = re.sub(r'\D', '', line)
    first_digit = int(digits_only[0])
    last_digit = int(digits_only[-1])

    result = int(str(first_digit) + str(last_digit))
    result_list.append(result)

print(sum(result_list))

