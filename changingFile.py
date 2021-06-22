# import time,sys, os

# os.system('cls')
# file="scoreboard.txt"
# FILE=open(file, 'r')
# print(FILE.read())
# # print(contest_List)
# FILE.close()
# FILE=open(file, 'r')
# contest_List=FILE.readlines()
# # for element in contest_List:
# #     print(element)
# # contest_List = FILE.readlines()
# #print(contest_List)
# # FILE.close()
# #sorted_List=sorted(contest_List, key=lambda x: int (x.split()[4])). reverse=True)
# sorted_List=sorted(contest_List, reverse=True)[::-1]

# for line in range(5):
#     print(sorted_List[line])

#Quentin
from hashlib import new
from os import write
import os

scoredat="scoreboardt.txt"
def pause():
    print("Press enter to contine:")
    input()
print("Scores Chosen")
with open(scoredat,'r') as first_file:#open score archive
    rows = first_file.readlines()
    sorted_rows = sorted(rows, key=lambda x: int(x.split()[4])), reverse=True)
    with open(scoredat,'w+') as second_file:
        for row in sorted_rows:
            second_file.write(row)
first_file.close()
second_file.close()
writenScores = open(scoredat, 'r')
displayScores = writenScores.read()
print(displayScores)
writenScores.close()
pause()