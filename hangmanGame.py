#Lucas Williams
#06/11/2021
#word game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed
# play as long as the user has turns or has guessed the word
# import random

# gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
# name = input("What is your name?")
# print(name, end= " ")
# answer = input("Do you want to play?").upper()
# print("\n",gameWords) #delete when code works properly
# while "Y" in answer:
#     print(name,"Good luck")
#     word=random.choice(gameWords)
#     print(word)
#     answer="n"
#     turns=10 # find better way to create turns in future
#     guesses=''
#     varOccurences= 0
#     counter=len(word)
#     var3 = counter
#     while turns >0 and counter>=0:
#         for char in word:
#             if char in guesses:
#                 print(char, end=' ')
#             else:
#                 print('_',end=' ')
#         newGuess=input("\n Give me a letter")
#         for x in range(0,var3-1):
#             if newGuess in word[x]:
#                 varOccurences += 1
#                 #print("it worked")
#         if newGuess in word: #going to have to check if it appears more than once in the word(the letter)
#             counter -= varOccurences # going to need to replace this with a var that counts how many times the letter appears in the word.
#                #guesses= guesses+newGuesses
#             print("you are Right!!", )
#             varOccurences= 0
#         else:
#             counter -=word.count(newGuess)
#             turns -= 1
#             print ("Sorry that is wrong you still have ", turns, " turns")
#         guesses += newGuess
#     answer="n"
#     print("Goodbye")

import random
import os
import sys
import time
import datetime

os.system('cls')
#Global Variable
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name = input("What is your name?")
print(name, end= " ")
# answer = input("Do you want to play?").upper()
score = 0
file="scoreboard.txt"
print("\n",gameWords) 
dt=datetime.datetime.now()
linef="\t"+str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year) +"\t"+dt.strftime("%A")+"\t"
def menu():
    print("*"*28)
    print("*"," "*3,"Choice 1 - Play"," "*4,"*")
    print("*"," "*3,"Choice 2 = Scores"," "*2,"*")
    print("*"," "*3,"Choice 3 = Exit"," "*4,"*")
    print("*"*28)
    return input("What is your choice? 1,2, or 3?")
def updateWord(word, guesses): #function with a parameter
    for char in word:
        if char in guesses:
            print(char,end='') 
        else:
            print('_', end =' ')
def printScore():
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close
    # Open the file and print the file
    print()
def updateScore(score):
    #open the file and update the score list
    #date Name Score
    fileWrite=open(file, 'a')
    x = datetime.datetime.now()
    line= name +"\t"+ linef +"\t"+ str(score)
    fileWrite.write("\n"+ line)
    fileWrite.close()
    print()
def playGame(answer, score):
    while "Y" in answer:
        print(name,"Good luck")
        word=random.choice(gameWords)
        print(word)
        turns=10 # find better way to create turns in future
        guesses=''
        counter=len(word)
        updateWord(word, guesses)
        while turns >0 and counter>0:
            newGuess=input("\n\nGive me a letter")
            if newGuess not in guesses:
                if newGuess not in word:
                    turns -=1   # turns = turns = -1
                    print("Wrong! You have ", turns, "guesses left")
                else:
                    counter -=word.count(newGuess) # delete repeated letters
                    print("Nice guess!")
                guesses += newGuess
            else:
                print("You already used this letter.")
            updateWord(word, guesses)
        if counter ==0:
            print("\nAmazing, you are the Champion")
            score += 1
        else:
            print("Sorry, try harder next time")
        answer = input("Do you want to play again?").upper()
    updateScore(score)
#your main program
check=True
while check:
    varChoice = menu()
    if "1" in varChoice:
        playGame("Y",score)
        time.sleep(2)
        os.system('cls')

    elif "2" in varChoice:
        printScore()
        time.sleep(6)
        os.system('cls')
    else:
        print("Thank you!")
        check=False
    time.sleep(2)
    os.system('cls')











# print(name,""" thank you for playing!
# You got""", score, "points")
# BOOK=open("scoreboard.txt", 'a')

# BOOK.write(name,end=" ")
# BOOK.write(x,end=" ")
# BOOK.write(score)
# time.sleep(1)
# BOOK.close()
# find a way to decide if the person won the game or not 
# keep a count of how many words they gussed   
# ask user if the want to play again


# Start my main program