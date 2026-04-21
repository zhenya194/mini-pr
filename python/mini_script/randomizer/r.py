import random

min_num: float = float(input("Write minimum number: "))
max_num: float = float(input("Write minimum number: "))
if min_num - int(min_num) == 0 and max_num - int(max_num) == 0:
    new_min_num = int(min_num)
    new_max_num = int(max_num)
    print(f"Random number: {random.randint(new_min_num, new_max_num)}")
else:
    print(f"Random number: {random.uniform(min_num, max_num)}")
