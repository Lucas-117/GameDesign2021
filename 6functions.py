#lucas Williams
# using six different list functions for homework
myNumber=[1,2,37,8,9]
keywords=["aegis","saint","palindrome","last wish"]
keywords.append("salvation")
print(keywords[0:5])
activationCode = keywords.copy()
for x in range (0,4): 
    print (keywords[x], end=", ")
print(keywords[4])
activationCode.reverse()
for x in range (0,4): 
    print (activationCode[x], end=", ")
print(activationCode[4])
activationCode.clear()
print(keywords,activationCode)
keywords.remove("aegis")
for x in range (0,3): 
    print (keywords[x], end=", ")
print(keywords[3])
activationCode.insert(1,"aegis")
print(activationCode)
keywords.sort()
for x in range (0,3): 
    print (keywords[x], end=", ")
print(keywords[3])