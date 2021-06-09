# game menu challenge 
# Lucas Williams
def gameover():
    print("*"*21)
    print("*"," "*1,"GAME COMPLETE"," "*1,"*")
    print("*"*21)
def score():
    print("*"*28)
    print("*"," "*5,"Lucas - 9999"," "*5,"*") # prints a scoreboard
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
menu() # calls the function
varTxt = "Failure try again, you have one more chance."
varTxt2 = "Failure try again, you have {} more chance."
varChoice = str(input())
while varChoice != "EX":
    if varChoice  == "E1":
        gap()
        print("Welcome to the first encounter, in order to progress you must enter the missing number in the sequence,") # challenges the user with a math problem
        print("5,8,13,21,__") # fibonacci
        varAnswer = str(input())
        if varAnswer == "34":
            print("Congratulatious you may proceed to next encounter") # tests if the user answered the question correctly if not gives them two more chances at redemption
            varChoice = "E2"
        else:# (technique from website) if else statement
            print("Failure try again, you have two more chances.")# see earlier comment
            varAnswer = str(input())
            if varAnswer == "34":
                print("Congratulatious you may proceed to next encounter")
                varChoice = "E2"
            else:
                if "Failure" in varTxt:# (technique from website) check string
                    print(varTxt2.format("one"))# (technique from website) format strings to insert characters
                    varAnswer = str(input())
                    if varAnswer == "34":
                        print("Congratulatious you may proceed to next encounter")# see earlier comment
                        varChoice = "E2"
                    else:
                        print("Failure.")
                        break

    if varChoice  == "E2":
        gap()# tests if the user answered the question correctly if not gives them two more chances at redemption
        print("""You have passed the Math Challenge and now the time has come to test your pop-culture knowledge,
        Complete this phase, \"_ _ _ shot first\"""")
        varAnswer = str(input())# (2 techniques from website)^^^^^ escape chracters \" and mutliples lines of text in a print statement
        varAnswer = varAnswer.lower()# (technique from website) modifying the string to lower case
        if varAnswer == "han":
            print("You have passed this encounter, you may procede to the final enocunter.") # allows them passge to the final encounter by changing the value of varChoice
            varChoice = "E3"
        else:
            print("Failure try again, you have two more chances.")
            varAnswer = str(input())
            if varAnswer == "han":
                print("You have passed this encounter, you may procede to the final enocunter.")
                varChoice = "E3"
            else:
                print("Failure try again, you have one more chance.")
                varAnswer = str(input())
                if varAnswer == "han":
                    print("You have passed this encounter, you may procede to the final enocunter.")
                    varChoice = "E3"
                else:
                    print("Failure.")
                    break

    if varChoice  == "E3":
        gap()
        print("You may have answered that question correctly, but tell me this,") # tests if the user answered the question correctly if not gives them two more chances at redemption
        print("What walks on four legs in the morning, two legs during the day, and three in the evening?")
        varAnswer = str(input())
        varAnswer = varAnswer.lower()
        if varAnswer == "man":
            print()
            print()
            print()
            print("Interesting, you have completed the trials, you may leave.") # decides the user has passed the trials
            break

        else:
            print("Failure try again, you have two more chances.")
            varAnswer = str(input())
            if varAnswer == "man":
                print()
                print()
                print()
                print("Interesting, you have completed the trials, you may leave.")
            else:
                print("Failure try again, you have one more chance.")
                varAnswer = str(input())
                if varAnswer == "man":
                    print()
                    print()
                    print()
                    print("Interesting, you have completed the trials, you may leave.")
                else:
                    print(varTxt[0:7])# (technique from website) slices to the string to only print part of it
                    break

    if varChoice  == "S":
        score()
    menu()
    varChoice = str(input())
gameover()

























































