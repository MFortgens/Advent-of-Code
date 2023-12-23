with open('input_day2.txt', 'r') as input:
    rounds = input.read().splitlines()

    ## PART 1
    combinations = {'A X' : 1 + 3,
                    'A Y' : 2 + 6,
                    'A Z' : 3 + 0,
                    'B X' : 1 + 0,
                    'B Y' : 2 + 3,
                    'B Z' : 3 + 6,
                    'C X' : 1 + 6,
                    'C Y' : 2 + 0,
                    'C Z' : 3 + 3
                    }
    
    score = 0
    for i in rounds:
        score += combinations[str(i)]
    
    print(score)

    ## PART 2
    combinations_p2 = {'A X' : 0 + 3,
                       'A Y' : 3 + 1,
                       'A Z' : 6 + 2,
                       'B X' : 0 + 1,
                       'B Y' : 3 + 2,
                       'B Z' : 6 + 3,
                       'C X' : 0 + 2,
                       'C Y' : 3 + 3,
                       'C Z' : 6 + 1
                      }

    score_p2 = 0
    for i in rounds:
        score_p2 += combinations_p2[str(i)]

    print(score_p2)