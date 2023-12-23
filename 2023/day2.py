import re

with open('input_day2.txt', 'r') as f:
    input = f.read().splitlines()

## PART 1
possible_games = []

while True:
    for i in input:
        game = re.findall(r'\d+ \w+', i)
        game_id = re.search(r'Game (\d+):', i)

        for cubes in game:
            num = re.search(r'\d+', cubes)
            color = re.search(r'[a-z]+', cubes)

            # Red
            if color.group() == 'red' and int(num.group()) > 12:
                break
            # Green
            elif color.group() == 'green' and int(num.group()) > 13:
                break
            # Blue
            elif color.group() == 'blue' and int(num.group()) > 14:
                break

        else:
            possible_games.append(game_id.group(1))
    break

sum_game_ids = sum([int(x) for x in possible_games])
print(f"The sum of possible game IDs is {sum_game_ids}")

## PART 2
sum_power = 0
for i in input:
    game = re.findall(r'\d+ \w+', i)
    red_max = 0
    green_max = 0
    blue_max = 0
    for cubes in game:
        num = re.search(r'\d+', cubes)
        color = re.search(r'[a-z]+', cubes)

        if color.group() == 'red':
            red_cube = int(num.group())
            if red_cube > red_max:
                red_max = red_cube
        if color.group() == 'green':
            green_cube = int(num.group())
            if green_cube > green_max:
                green_max = green_cube
        if color.group() == 'blue':
            blue_cube = int(num.group())
            if blue_cube > blue_max:
                blue_max = blue_cube
    
    sum_power += red_max * green_max * blue_max

print(f"The sum of the power is {sum_power}")


