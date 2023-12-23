with open('input_day1.txt', 'r') as input:
    lines = input.read().split('\n\n')

    elves = []
    for line in lines:
        elves.append(line.split())
    
    sumfood = []
    for elf in elves:
        calories = []
        for food in elf:
            calories.append(int(food))
        sumfood.append(sum(calories))
    sumfood.sort(reverse=True)
    print(sumfood)

    top3 = sum(sumfood[:3])
    print(top3)