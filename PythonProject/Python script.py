
import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Open the results.txt file for writing
with open('results.txt', 'w') as file:
    for num in range(1, 251):
        if is_prime(num):
            # Print the prime number to the console
            print(num)
            # Write the prime number to the file
            file.write(str(num) + '\n')