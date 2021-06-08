#game menu challenge 
#Lucas Williams
def menu():
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Two Betrayls"," "*4,"*")
    print("*"," "*2,"L2- Sacred Icon"," "*5,"*")
    print("*"," "*2,"L3- The Storm"," "*7,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")
menu() #calls the function
varChoice = str(input())
while varChoice != "EX":
    menu()
    varChoice = str(input())
print("Goodbye, Have a nice day")






















































































