#using a string in which the index will determine proper priority
priorities = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# thought this was cool so im stashing it here for future reference.
# def convertCharToInt(c):
#     return ord(c) - 96 if c.islower() else ord(c) - 38

def intersection(lst1, lst2, lst3):
    inter = list(set(lst1) & set(lst2) & set(lst3))
    inter.remove('\n')
    return inter

with (open("day3/input.txt")) as input:
    sum_priority = 0
    lines = input.readlines()

    for i in range(0, len(lines), 3):
        common_type = intersection(lines[i], lines[i+1], lines[i+2])
        common_type_priority = priorities.index(common_type[0])
        sum_priority += common_type_priority

    print(sum_priority)
