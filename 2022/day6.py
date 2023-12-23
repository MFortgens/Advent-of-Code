with open('input_day6.txt') as f:
    input = f.read().strip()

    distinct_chars = [4, 14]
    for num in distinct_chars:
        for i in range(num, len(input)):
            marker = set(input[i:i+num])
            if len(marker) == num:
                print(f'The first marker can be found after character: {i + num}')
                break