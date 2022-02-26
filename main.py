# Group 22A3 - Sprint Week Program
# Written by Glen May, Mark Hannem & Jacob Eagles
# Written between February 25th 2022 and March 6th 2022
# This program does, uh, what?

# Make sure to install "pip install MatPlotLib" in the terminal
import matplotlib.pyplot as plt

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


def Graph():
    # Function for Graph
    Mths = ["Jan", "Feb", "Mar", "Apr'", "May", "June", "July", "Aug",
            "Sept", "Oct", "Nov", "Dec"]

    # Define Plot Space
    fig, ax = plt.subplots(figsize=(12, 8))

    # Formatting x/y-axis, titles and graph
    xaxis = Mths
    yaxis = Sales

    ax.plot(xaxis, yaxis, color="cyan", marker="o")

    plt.xlabel("Months", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.ylabel("Monthly Totals\n(dollars,$)", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.setp(ax.get_xticklabels(), rotation=45)

    plt.title("NL Chocolate Company\nSales Totals Per Month", fontdict={'fontsize': 15,
                                                                        'fontweight': 5, 'color': 'darkgoldenrod'})
    plt.grid(True)

    plt.show()

    return plt.show()


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
        Sales = []
while True:
    print("Input Your Monthly Sales Total Below")
    print()

    while True:
        try:
            Jan = float(input("Enter the Total Sales For January: "))
        except:
            print("January must have a valid number entry please - re-enter.")
        else:
            Sales.append(Jan)
            break
    while True:
        try:
            Feb = float(input("Enter the Total Sales For February: "))
        except:
            print("February must have a valid number entry please - re-enter.")
        else:
            Sales.append(Feb)
            break
    while True:
        try:
            Mar = float(input("Enter the Total Sales For March: "))
        except:
            print("March must have a valid number entry please - re-enter.")
        else:
            Sales.append(Mar)
            break
    while True:
        try:
            Apr = float(input("Enter the Total Sales For April: "))
        except:
            print("April must have a valid number entry please - re-enter.")
        else:
            Sales.append(Apr)
            break
    while True:
        try:
            May = float(input("Enter the Total Sales For May: "))
        except:
            print("May must have a valid number entry please - re-enter.")
        else:
            Sales.append(May)
            break
    while True:
        try:
            Jun = float(input("Enter the Total Sales For June: "))
        except:
            print("June must have a valid number entry please - re-enter.")
        else:
            Sales.append(Jun)
            break
    while True:
        try:
            Jul = float(input("Enter the Total Sales For July: "))
        except:
            print("July must have a valid number entry please - re-enter.")
        else:
            Sales.append(Jul)
            break
    while True:
        try:
            Aug = float(input("Enter the Total Sales For August: "))
        except:
            print("August must have a valid number entry please - re-enter.")
        else:
            Sales.append(Aug)
            break
    while True:
        try:
            Sep = float(input("Enter the Total Sales For September: "))
        except:
            print("September must have a valid number entry please - re-enter.")
        else:
            Sales.append(Sep)
            break
    while True:
        try:
            Oct = float(input("Enter the Total Sales For October: "))
        except:
            print("October cannot be blank.")
        else:
            Sales.append(Oct)
            break
    while True:
        try:
            Nov = float(input("Enter the Total Sales For November: "))
        except:
            print("November must have a valid number entry please - re-enter.")
        else:
            Sales.append(Nov)
            break
    while True:
        try:
            Dec = float(input("Enter the Total Sales For December: "))
        except:
            print("December must have a valid number entry please - re-enter.")
        else:
            Sales.append(Dec)
            break
    break
        Graph()
        
    elif userChoice == "5":
        quit()
    else:
        print("Try again?")
