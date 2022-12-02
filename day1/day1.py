
#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
with open('day1/input.txt') as input:
    elf_total = 0
    totals = []

    lines = input.readlines()
    for line in lines:
        if line == '\n':
            totals.append(elf_total)
            # reset elf_total when new elf is reached
            elf_total=0
        else:
            line = int(line)
            elf_total += line

    totals.sort(reverse=True)

#part 1 answer : 
print(totals[0])

#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
#part 2 answer : 
print(totals[0] + totals[1] + totals[2])