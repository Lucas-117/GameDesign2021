# Lucas Williams
# use different types of varibles
# Use Strings functions
# Use while loop

num1=10
num2=3.5
num3=0xADFE7878347658374658347658374653847568365834765834765873465873465873465836578456823462745723457236457623547632547623746523764523764527345237645273645237645237645237645237645237645237465237643523746523746253476253476235472635427365476235472364523745276345273645726457236457236452736452376452376452376452376452376452376452374625472354723645237465237462354726345732645237465237645237645237645327465237423654723645237465237462357462354762354723645237645237645723654732645237645237645327645237642364532423423423424324234324234756834756843756834563487563487563485634878ADF788787EADFB
name="Computer"
#   0123456789 last index is 7 len=8
print(type(num1))
print(type(num2))
print(type(num3))
print(type(name))
print(name[2]) #Prints the letter at index 2
print(name[2:7]) #print set of letter from 2 to 6
numIndex=len(name)
print (numIndex)
print(name[2:],end=" ")   #print from 3 to the end
print()
print(name*5)
# for var in range(1,5):
#     print(name[3:numIndex])   #print from 3 to the end
#     print(name[3:numIndex-var])
# print ("Done")

#concatenation
name="Peter"
lastName= "Smith"
print(name," ",lastName)
fullName= name + " " + lastName + "/"
print(fullName)
print("Smith" in fullName)
while "Smith" in fullName:
    print(fullName)
    fullName=fullName+"2"
    var= random.randint(1:10)
    print (var)
print("Done")