import random

big_number = 100000

def roll(x):
    result = []
    if x != 0:
        for y in range(x):
            result.append(random.randrange(1,7))
        if result.count(6) > 1:
            return 4
        elif max(result) > 5:
            return 3
        elif max(result) > 3:
            return 2
        else:
            return 1
        return max(result)
    else:
        for y in range(2):
            result.append(random.randrange(1,7))
        if min(result) > 5:
            return 3
        elif min(result) > 3:
            return 2
        else:
            return 1
successes = 0

for x in range(big_number):
    if roll(2) + roll(2) + roll(2) > 3:#modify this line appropriately
        successes+=1

print(successes/big_number)
input()