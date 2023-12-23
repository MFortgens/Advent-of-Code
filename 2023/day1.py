import re

with open('input_day1.txt', 'r') as f:
    input = f.read().splitlines()

## PART 1
calibrations = []
for i in input:
    digits = re.findall(r'\d', i)
    calibrations.append(digits[0] + digits[-1])

sum_calibrations = sum([int(x) for x in calibrations])
print(f"The sum of all the calibration values is: {sum_calibrations}")

print(calibrations)
## PART 2

text = 'vqjvxtc79mvdnktdsxcqc1sevenone'

# https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
# https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
# https://www.reddit.com/r/adventofcode/comments/1883ibu/2023_day_1_solutions/