Year_start = int(input("What year do you want to start with?"))
Num_of_years = int(input("How many years do you want to check?"))

for t in range(Year_start, Year_start + Num_of_years):
    if (t % 4) == 0:  
        print (f"{t} is a leap year")  
    else:  
       print (f"{t} is not a leap year")1