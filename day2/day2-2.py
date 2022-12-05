# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

throwPoints = {
    "X": 1,  # rock
    "A": 1,
    "Y": 2,  # paper
    "B": 2,
    "Z": 3,  # scissors
    "C": 3
}

#part2
with open('day2/input.txt') as input:
    scoreTally = 0
    lines = input.readlines()
    
    for line in lines:
        round = line.split(' ')
    #outcomes
        if throwPoints[line[2]] == 1:
            scoreTally+=0 #lose
        elif throwPoints[line[2]] == 2:
            scoreTally+=3 #draw
        elif throwPoints[line[2]] == 3:
            scoreTally+=6 #win
    #lose
        if throwPoints[line[0]] == 1:
            if throwPoints[line[2]] == 1:
                scoreTally += 3 #scissors
            elif throwPoints[line[2]] == 2:
                scoreTally += 1 #rock
            elif throwPoints[line[2]] == 3:
                scoreTally += 2 #paper
    #draw
        elif throwPoints[line[0]] == 2:
            if throwPoints[line[2]] == 1:
                 scoreTally += 1 #rock
            elif throwPoints[line[2]] == 2:
                 scoreTally += 2 #paper
            elif throwPoints[line[2]] == 3:
                scoreTally += 3 #scissors
    #win
        elif throwPoints[line[0]] == 3:
            if throwPoints[line[2]] == 1:
                scoreTally += 2 #paper    
            elif throwPoints[line[2]] == 2:
                scoreTally += 3 #scissors
            elif throwPoints[line[2]] == 3:        
                scoreTally += 1 #rock
print(scoreTally)