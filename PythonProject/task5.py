    print(y)                            # print y
    y+=1                                # y = y +1

z=1                                         # set loop at 1
while z<21:
    print(z*"*")                            # print '*' * z
    z+=1                                    # z = z + 1       

####
GCD Greatest common divisor of two positive integeers
###

a=int(input("Input your 1st Number :"))     # Get input from user as number
b=int(input("Iput Your 2nd Number :"))      # Get input from user as number b

def gcd(a,b):                               # define GCD  function
    if a % b == 0:                          # if a i diasior b is 0
        return b                            # then return b
    for c in range (int(b/2),0,-1):         # if a is not divisable by b it enters a for loop.
    if a % c == 0 and b % c ==0             # c checks if a and b are common divisors.
        gcd=c                               # and if it is thec is set as var of gcd
        break                               # break out of loop
    return gcd                              # returns the fuctions of gcd a and b
print("GCD of",a,"and",b,"=",gcd(a,b))       # Prints the GCD 
      
