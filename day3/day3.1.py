#Day 3.1 adventofcode.com 2023
symbols = set("!@#$%^&*()/,;'[]{+}=-|")

input = open("day3/input.txt")
lines = input.read().split('\n')

lines_with_dots = ['.' + line + '.' for line in lines]
modified_input = ''.join(lines_with_dots)
line_length = len(lines_with_dots[0])
modified_input = ("." * line_length) + modified_input + ("." * line_length)

temp_num = ''
engine_number_list = []
num_next_to_symbol = False

for i in range(line_length, len(modified_input) - line_length):
    if modified_input[i].isnumeric():
        temp_num += modified_input[i]
        adjacent_symbols = [
            modified_input[i - 1],
            modified_input[i + 1],
            modified_input[(i + line_length) - 1],
            modified_input[(i + line_length) + 1],
            modified_input[(i - line_length) - 1],
            modified_input[(i - line_length) + 1],
            modified_input[i + line_length],
        ]

        if any(symbol in symbols for symbol in adjacent_symbols):
            num_next_to_symbol = True
    else:
        if num_next_to_symbol:
            engine_number_list.append(temp_num)
        num_next_to_symbol = False
        temp_num = ''

print(sum(map(int, engine_number_list)))