# Written by Mark Hannem on February 27th

# Program Edited on Feb 27th, 28th and March 1st

# Function that solves the "FizzBuzz" interview question
def fizzbuzz():
    # For Loop with Range 1 to 100 displaying Fizz,Buzz or FizzBuzz for numbers
    # divisible by 5 & 8, 5 and 8 respectively
    # This function acts as the main program
    for Num in range(1, 101):
        if Num % 5 == 0 and Num % 8 == 0:
            print("FizzBuzz")
        elif Num % 5 == 0:
            print("Fizz")
        elif Num % 8 == 0:
            print("Buzz")
        else:
            print(Num)