import random

random_list = [random.randrange(1, 101, 1) for i in range(100)]

even = 0
odd = 0
for number in random_list:
    if (number % 2) == 0:
        even += 1
    else:
        odd += 1

print(f"There are {even} even, and {odd} odd numbers in a random list")
