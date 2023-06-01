#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = lastDigit * -1
validation = (
    "and is greater than 5"
    if lastDigit > 5
    else "and is 0"
    if lastDigit == 0 else "and is less than 6 and not 0")
print("Last digit of {} is {} {}".format(number, lastDigit, validation))
