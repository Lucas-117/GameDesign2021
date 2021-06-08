# Lucas Williams
# this program is meant for printing multiplacation tables
# Using print statements and a varibles
# input ---> from the user
# use the function input()
# variables need to have vaild name
from typing import Counter



print("enter a number")
base = int(input())
print("Addition Table for", base)
for counter2 in range(1,11):   #intital value included and ending value that is not included
    print(base, "+", counter2, "=", base + counter2)
print("Subtraction Table for", base)
for counter2 in range(1,11):   #intital value included and ending value that is not included
    print(base, "-", counter2, "=", base - counter2)
print("Multiplication Table for", base)
for counter2 in range(1,11):   #intital value included and ending value that is not included
    print(base, "x", counter2, "=", base * counter2)
print("Divison Table for", base)
for counter2 in range(1,11):   #intital value included and ending value that is not included
    print(base, "/", counter2, "=", base / counter2)



























































































