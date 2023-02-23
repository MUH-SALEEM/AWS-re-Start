myString = input("Input a string: ")   #input for string
alternateString = ""  #blank string to store the string with alternate characters capital and small
#loop to convert the letters to upper case and lower case
for i in range(len(myString)):
    if i % 2 == 0:
        alternateString = alternateString + myString[i].upper()
    else:
        alternateString = alternateString + myString[i].lower()
print(alternateString)
