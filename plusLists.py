# Lucas Williams
# lists and their functions
#indexing a list always start in 0
from typing import Counter


myNumber=[1,2,37,8,9]
myFruits=["apples","kiwis","mango", "banana"]
print(myFruits)
myFruits.append("strawberry")
for x in myFruits: # for each element in your array get the value
    print (x, end=", ")
print()
counter=len(myFruits)
for x in range (0,counter-1): #length of array one more tha last index
#for loop limit your array order
    print (myFruits[x], end=", ")
print(myFruits[counter-1])
myFruits[1]="berries"
print (myFruits[1:3])
if "apples" in myFruits:
    print("I got apples")
else:
    print("I need apples")

