import re

with open('input_day4.txt', 'r') as f:
#     input = f.read().splitlines()
    # # sections_to_clean = [[range(int(sections.split('-')[0]), int(sections.split('-')[1]) + 1) for sections in line.split(',')] for line in f]
    # # print(sections_to_clean)


    # pairs = []
    for line in f:
        pairs = line.strip().split(',')
        print(pairs)





        sections = []
        for section in pairs:
            sections.append(re.findall('\d+', section))
        print(sections)

        for i in sections:






        pairs.append(line.strip().split(','))

    for section in pairs:
        section_range = re.findall('\d+', section)
        print(section_range)




        print(range(int(section.split('-')[0]), range(int(section.split('-')[1]))) + 1)





    count = 0
    for pair in input:






test = '23-54,22-55'

for i in test:
    print(i)



# for i in range(94, 97+1):
#     print(i)


# s1 = set([1,2,3,4,5])
# s2 = set([2,3,4])

# check = s2.issubset(s1)
# print(check)

# if true > + 1