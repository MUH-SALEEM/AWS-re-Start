InputString=input("Input a string : ")
SetOfCharacters=input("Input the characters which are to be deleted : ")
newString=""
for i in InputString :
 if i not in SetOfCharacters:
  newString=newString+i

print(newString)