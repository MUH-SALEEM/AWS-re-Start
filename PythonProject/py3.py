# function to check if a number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# list to store prime numbers
primes = []

# find all prime numbers between 1 and 250
for num in range(1, 251):
    if is_prime(num):
        primes.append(num)
        
        # write results to file
with open("results.txt", "w") as f:
    for prime in primes:
        f.write(str(prime) + "\n")

# print results to console
print("Prime numbers between 1 and 250:")
print(primes)
