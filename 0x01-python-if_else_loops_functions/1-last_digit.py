#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit < 6 and digit != 0 or number < 0:
    print(f"Last digit of {number} is {digit} and is less 6 and not 0")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
