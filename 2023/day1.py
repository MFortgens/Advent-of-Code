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
