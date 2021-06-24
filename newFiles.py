#Lucas Williams
#06/14/2021
#We are going to learn how to open files, read files, write to files

import os
import sys
import time
# print("Hello... let me guess your name ...")
# time.sleep(2)
# print("... almost...")
# print("... Yes, you are Lucas")
# time.sleep(2)
# os.system('cls')
# file=input("Please enter the file name add extension of the file. Ex file.txt :")
# #check if the file exists
# if os.path.exists(file):
#     PENCIL= open(file,'r')
#     print(PENCIL.read())
#     PENCIL.close()
# else:
#     print ("The file does not exist")
BOOK=open("samplefile.txt", 'a')
BOOK.write("\n this is writing")
time.sleep(1)
BOOK.close()