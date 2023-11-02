#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = str(number)
    last_digit = last_digit[-1]
    last_digit = int(last_digit)
    last_digit = -(last_digit)
else:
    last_digit = str(number)
    last_digit = last_digit[-1]
    last_digit = int(last_digit)

output = "Last digit of {} is {} and is"
output1 = "greater than 5"
outout2 = "0"
output3 = "less than 6 and not 0"

if last_digit > 5:
    print(output.format(number, last_digit), output1)
elif last_digit == 0:
    print(output.format(number, last_digit), output2)
else:
    print(output.format(number, last_digit), output3)
