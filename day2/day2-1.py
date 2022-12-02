# What would your total score be if everything goes exactly according to your strategy guide?

throwPoints = {
    "X": 1,  # rock
    "A": 1,
    "Y": 2,  # paper
    "B": 2,
    "Z": 3,  # scissors
    "C": 3
}

#part 1
with open('day2/input.txt') as input:
    scoreTally = 0
    lines = input.readlines()
    for line in lines:
        round = line.split(' ')
    #score tally for each throw value
        scoreTally += throwPoints[line[2]]
    #outcomes
        #rock
        if throwPoints[line[2]] ==1:
            if throwPoints[line[0]] == 1:
                scoreTally+=3
            elif throwPoints[line[0]] == 2:
                scoreTally+=0
            if throwPoints[line[0]] ==3:
                scoreTally+=6
        #paper
        elif throwPoints[line[2]] == 2:
            if throwPoints[line[0]] == 1:
                scoreTally+=6
            elif throwPoints[line[0]] == 2:
                scoreTally+=3
            if throwPoints[line[0]] ==3:
                scoreTally+=0
        #scissors
        elif throwPoints[line[2]] == 3:
            if throwPoints[line[0]] == 1:
                scoreTally+=0
            elif throwPoints[line[0]] == 2:
                scoreTally+=6
            if throwPoints[line[0]] ==3:
                scoreTally+=3
print(scoreTally)


