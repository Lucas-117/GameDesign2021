#Lucas Williams
#06/11/2021
#word game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed
# play as long as the user has turns or has guessed the word
import random

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name = input("What is your name?")
print(name, end= " ")
answer = input("Do you want to play?").upper()
print("\n",gameWords) #delete when code works properly
while "Y" in answer:
    print(name,"Good luck")
    word=random.choice(gameWords)
    print(word)
    answer="n"
    turns=10 # find better way to create turns in future
    guesses=''
    varOccurences= 0
    counter=len(word)
    while turns >0 and counter>=0:
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_',end=' ')
        newGuess=input("\n Give me a letter")
        for x in range(0,counter-1):
            if newGuess in word[x]:
                varOccurences += 1
                #print("it worked")
        if newGuess in word: #going to have to check if it appears more than once in the word(the letter)
            counter -= varOccurences # going to need to replace this with a var that counts how many times the letter appears in the word.
            guesses += newGuess   #guesses= guesses+newGuesses
            print("you are Right!!", )
            varOccurences= 0
        else:
            turns -= 1
            print ("Sorry that is wrong you still have ", turns, " turns")
    answer="n"
    print("Goodbye")