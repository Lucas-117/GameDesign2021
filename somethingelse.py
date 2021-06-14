import random
myFruits=["apples","kiwis","mango", "banana"]
indx=random.randint(0,4)
print(indx)
print("your lucky fruit is ", myFruits[indx])
word=random.choice(myFruits[indx])
print("your lucky fruit is ", word)