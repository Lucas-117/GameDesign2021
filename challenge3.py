#lucas Williams
# Challenge 3
def menu():
    print("*"*29)
    print("*"," "*5,"1Append salvation"," "*1,"*") # prints a scoreboard (consider modifying later based on user input?)
    print("*"," "*5,"2Remove Aegis"," "*5,"*")
    print("*"," "*5,"3Find Aegis"," "*7,"*")
    print("*"," "*5,"4Locate Aegis"," "*5,"*")
    print("*"," "*5,"5Reverse the order"," *")
    print("*"," "*5,"EX - Exit the list"," *")
    print("*"*29)
menu()
varChoice = str(input())
while varChoice != "EX":
    keywords=["aegis","saint","palindrome","last wish"]
    if varChoice == "1":
        keywords.append("salvation")
    if varChoice == "2":
        keywords.remove("aegis")
    if varChoice == "3":
        if "aegis" in keywords:
            print("aegis is in the list")
    if varChoice == "4":
        keywords.index("aegis")
    if varChoice == "5":
        keywords.reverse()
    # print(keywords[0:5])
    # activationCode = keywords.copy()
    # for x in range (0,4): 
    #     print (keywords[x], end=", ")
    # print(keywords[4])
    # activationCode.reverse()
    # for x in range (0,4): 
    #     print (activationCode[x], end=", ")
    # print(activationCode[4])
    # activationCode.clear()
    # print(keywords,activationCode)
    # keywords.remove("aegis")
    # for x in range (0,3): 
    #     print (keywords[x], end=", ")
    # print(keywords[3])
    # activationCode.insert(1,"aegis")
    # print(activationCode)
    # keywords.sort()
    # for x in range (0,3): 
    #     print (keywords[x], end=", ")
    # print(keywords[3])
    # varChoice = str(input())
    print("to add another modifcation type a number, to leave type EX")
    varChoice = str(input())
counter=len(keywords)
for x in range (0,counter-1): #length of array one more tha last index
#for loop limit your array order
    print (keywords[x], end=", ")
print(keywords[counter-1])