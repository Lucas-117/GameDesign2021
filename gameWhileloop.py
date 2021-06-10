# game menu challenge 
# Lucas Williams
def gameover():
    print("*"*21)
    print("*"," "*1,"GAME COMPLETE"," "*1,"*")
    print("*"*21)
def score():
    print("*"*28)
    print("*"," "*5,"Lucas - 9999"," "*5,"*") # prints a scoreboard (consider modifying later based on user input?)
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"," "*5,"Lucas - 9999"," "*5,"*")
    print("*"*28)
def menu():
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*") # prints the main menu
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"E1- Two Betrayals"," "*3,"*")
    print("*"," "*2,"E2- Sacred Icon"," "*5,"*")
    print("*"," "*2,"E3- The Storm"," "*7,"*")
    print("*"," "*2,"E4- Prepare to Drop"," "*7,"*")
    print("*"," "*2,"E5- Long Night of Solace"," "*7,"*")
    print("*"," "*2,"S- List Scores"," "*6,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either E1,E2,E3,S, or EX", end= " ")
def gap():
    print() # creates a space for a more pleasing U.I.
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
def gamePause():
    print("do you want to play again?")
    level = input().upper()
    if "Y" in level:
        return True
    else:
        return False
varChoice=menu()

menu() # calls the function
varTxt = "Failure try again, you have one more chance."
varTxt2 = "Failure try again, you have {} more chance."
while varChoice != "EX":
    x=menu()
    if (x==1):
        convert = True #boolean Variable True or False
        while convert:
            print("You are in level 1")
            print("Please enter a phrase in lower case")
            answer = input()
            answer = answer.capitalize() #update your variable to the new changes
        #print(answer.capitalize())
            print(answer)
            convert = pause()

        # Let the user stay in the level and reuse it many times until they wan
    if (x==2):
        print("Level 2 ")








































