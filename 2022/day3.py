import string

with open('input_day3.txt', 'r') as f:
    input = f.read().splitlines()

    # Create list of item errors
    errors = []
    for rucksack in input:
        compartment1 = rucksack[:len(rucksack)//2]
        compartment2 = rucksack[len(rucksack)//2:]

        s1 = set(compartment1)
        s2 = set(compartment2)

        errors.extend(list(s1.intersection(s2)))

    # Assign values to letters
    values = {}
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27

    # Calculate priority sum
    priority_sum = 0
    for error in errors:
        priority_sum += values[error]
    
    print(f'The sum of the item priorities is: {priority_sum}')

    ## PART 2
    groups = []
    for r in range(0, len(input), 3):
        groups.append(input[r:r+3])

    badges_priority_sum = 0
    for group in groups:
        badges = []
        badges.extend(list(set.intersection(*map(set,group))))

        for badge in badges:
            badges_priority_sum += values[badge]

    print(f'The sum of the badge item priorities is: {badges_priority_sum}')