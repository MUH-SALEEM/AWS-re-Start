x = input("Enter a string: ")       #input for string
for char in x:
    if char == " ":                 #if the character in the sentence is a blank space, move to the next line
        print()
    else:                            #print character if it is not a blank space
        print(char, end = "")
        