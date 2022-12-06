with open('day4/input.txt') as input:
    lines = input.readlines()
    total_part1 = 0
    total_part2 = 0

    def intersection(lst1, lst2):
        return list(set(lst1) & set(lst2))

    for line in lines:
        pair = line.split(',')
        first_elf_section, second_elf_section = pair[0].split('-'), pair[1].split('-')

        #lists containing the ranges of the sections
        first_elf_range = []
        second_elf_range = []

        #build ranges for each line
        for i in range(int(first_elf_section[0]), int(first_elf_section[1])+1):
            first_elf_range.append(i)
        for i in range(int(second_elf_section[0]), int(second_elf_section[1])+1):
            second_elf_range.append(i)   

        #part 1      
        if all(section in first_elf_range for section in second_elf_range) or all(section in second_elf_range for section in first_elf_range):
            total_part1 += 1

        #part2   
        if intersection(first_elf_range, second_elf_range):
            total_part2 += 1

print(total_part1)
print(total_part2)
           