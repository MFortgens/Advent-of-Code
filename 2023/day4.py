import re

def intersection(input):
    input_nums = re.sub(r'Card\s+\d+:', '', i)
    win, num = input_nums.split('|')
    win_set = set(re.findall(r'\d+', win))
    num_set = set(re.findall(r'\d+', num))
    intersect_nums = win_set.intersection(num_set)
    return intersect_nums

def scorer(intersect):
    if len(intersect) == 0:
        score = 0
    elif len(intersect) == 1:
        score = 1
    else:
        score = 2**(len(intersect)-1)
    return score

with open('input_day4.txt', 'r') as f:
    input = f.read().splitlines()

## PART 1
total_score = 0
for i in input:
    total_score += scorer(intersection(i))

print(f"The total score of all the scratchcards is {total_score}")

## PART 2
score_list = [1] * len(input)

for index, nums in enumerate(input):
    input_nums = re.sub(r'Card\s+\d+:', '', nums)
    win, num = input_nums.split('|')
    win_set = set(re.findall(r'\d+', win))
    num_set = set(re.findall(r'\d+', num))
    num_matches = len(win_set.intersection(num_set))
    for card_num in range(index + 1, index + 1 + num_matches):
        score_list[card_num] += score_list[index]

print(f"The total number of scratchcards is {sum(score_list)}")
print(score_list)