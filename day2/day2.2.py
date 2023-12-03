#Day 2.2 adventofcode.com 2023
input = open("day2/input.txt")
read = input.read()

cube_counts = {"green":1, "red":1, "blue":1}

games = read.split("\n")
meets_requirements = True

sum = 0
result = 1

for game in games:
    lines = game.split(':')
    game_id = int(lines[0].split()[1])

    lines_prepared = lines[1].split(';')
    for line in lines_prepared:
        for color in line.split(","):
            parts = color.split()
            count, color = (int(parts[0]),parts[1])
            if cube_counts[color] < count or cube_counts[color] == 1:
                cube_counts[color] = count

    game_power = cube_counts["green"] * cube_counts["red"] * cube_counts["blue"]
    sum += game_power

    cube_counts.update({}.fromkeys(cube_counts,1))

print(sum)