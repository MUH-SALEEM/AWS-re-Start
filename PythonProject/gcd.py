n = 20
print("Countdown from 20 to 0:")        
while n >= 0:                               #loop to print countdown
    print(n, " ", end = "")
    n = n - 1
print()  
print("Input Even number between 0 and 20,: ")
for i in range(21):                         #loop to print even numbers from 0 to 20, both inclusive
    if i%2 == 0:
        print(i, " ", end = " ")
print("\nPattern: ")                        #loops to print the patter     
for i in range(6):
    for j in range(i):
        print("*", end ="")
    print()    
print("GCD:")
a = int(input("Input first number: "))       #code to find GCD of two numbers
b = int(input("Input second number: "))
x = 1
while x <= a and x <= b:
    if a % x == 0 and b % x == 0:
        gcd = x
    x = x + 1
print("The GCD of ", a, "and ", b, "is ", gcd)


