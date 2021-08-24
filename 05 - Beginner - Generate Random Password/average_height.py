import random
from functools import reduce

student_heights = [random.randint(140, 200) for i in range(101)]
print(student_heights)
print(f"Average heights is: ", round(reduce(lambda a, b: a + b, student_heights) / len(student_heights)))

print(globals())
