# Group 22A3 - Sprint Week Program
# Written by Glen May, Mark Hannem & Jacob Eagles
# Written between February 25th 2022 and March 6th 2022
# This program does, uh, what?

# Function for calculating travel claims for NL Chocolate Factory
def travelClaim():
    print("Travel Claim Program")

# Function that solves the "FizzBang" interview question
def fizzBang():
    print("FizzBang!")

# Function for a "cool program with Strings and Dates"
def strDate():
    print("Cool stuff")

# Function that graphs total sales?
def graphClaim():
    print("Graph")


#Main menu/program
print("NL Chocolate Company")

print("Travel Claims Processing System")
print("")
print("1. Enter an Employee Travel Claim.")
print("2. Fun Interview Question.")
print("3. Cool Stuff with Strings and Dates.")
print("4. Graph Monthly Claim Totals.")
print("5. Quit Program.")
print("")

while True:
    userChoice = input("   Enter Choice (1-5): ")
    if userChoice == "":
        print("Entry cannot be blank.")
    elif (userChoice.isnumeric()) ==  False:
        print("Entry not recognized.")
    elif int(userChoice) > 5:
        print("Entry not recognized.")
    elif int(userChoice) == 0:
        print("Entry not recognized.")
    elif userChoice == "1":
        travelClaim()
    elif userChoice == "2":
        fizzBang()
    elif userChoice == "3":
        strDate()
    elif userChoice == "4":
        graphClaim()
    elif userChoice == "5":
        quit()
    else:
        print("Try again?")