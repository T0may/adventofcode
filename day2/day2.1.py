#Day 2.1 adventofcode.com 2023
input = open("day2/input.txt")
read = input.read()


cube_counts = {"green":0, "red":0, "blue":0}
max_cuntes = {"green":13, "red":12, "blue":14}

moves = read.split("\n")
is_possible = True

id_sum = 0
for move in moves:
    lines = move.split(':')
    game_id = int(lines[0].split()[1])

    lines_prepared = lines[1].split(';')
    for line in lines_prepared:
        for color in line.split(","):
            parts = color.split()
            count, color = (int(parts[0]),parts[1])
            cube_counts[color] += count

        if any(cube_counts[color] > max_cuntes[color] for color in cube_counts):
            is_possible = False

        cube_counts.update({}.fromkeys(cube_counts,0))

    if is_possible:
        id_sum += game_id
    is_possible = True

print(id_sum)
