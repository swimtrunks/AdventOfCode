#using a string in which the index will determine proper priority
priorities = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# thought this was cool so im stashing it here for future reference.
# def convertCharToInt(c):
#     return ord(c) - 96 if c.islower() else ord(c) - 38

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

with open('day3/input.txt') as input:
    lines = input.readlines()
    sum_priority = 0

    for line in lines:
        half_length = len(line) // 2
        first_compartment, second_compartment = line[:half_length], line[half_length:]
        common_type = intersection(first_compartment, second_compartment)
        common_type_priority= priorities.index(common_type[0])

        sum_priority+=common_type_priority
    
    print(sum_priority)
