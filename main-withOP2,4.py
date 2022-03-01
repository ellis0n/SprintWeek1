# Group 22A3 - Sprint Week Program
# Written by Glen May, Mark Hannem & Jacob Eagles
# Written between February 25th 2022 and March 6th 2022
# This program does, uh, what?

import matplotlib.pyplot as plt


# Main Menu Function
def main():
    print("NL Chocolate Company")

    print("Travel Claims Processing System")
    print("")
    print("1. Enter an Employee Travel Claim.")
    print("2. Fun Interview Question.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")
    print("")


# Function for calculating travel claims for NL Chocolate Factory
def travelClaim():
    print("Travel Claim Program")


# Function that solves the "FizzBuzz" interview question
def fizzbuzz():
    for Num in range(1, 101):
        if Num % 5 == 0 and Num % 8 == 0:
            print("FizzBuzz")
        elif Num % 5 == 0:
            print("Fizz")
        elif Num % 8 == 0:
            print("Buzz")
        else:
            print(Num)


# Function for a "cool program with Strings and Dates"
# This function was written for the NL Chocolate Company.
# Calculates and determines employee eligibility to year-end bonus pay-outs.
# Bonuses included: standard, longevity, retention, retirement and tenure.
# Please see Technical Manual for further clarification on company policy.
# Written by Glen May on February 27, 2022.
def strDate():

    from datetime import datetime as dt
    from datetime import timedelta as td

    STANDARD_BONUS = 350.00  # Payable to employees after 2 years of employment..
    LON_BONUS = 50.00  # Replaces the standard bonus at 8 years of employment. Paid per year of employment.
    SERVICE_CAP = 20  # Longevity bonus yearly multiplier limit.
    RETIRE_CAP = 65  # Company policy for mandatory retirement at age 65.
    RETIRE_BONUS = 100.00  # Replaces standard and longevity bonus and is paid on retirement.
    TENURE_BONUS = 200.00  # Paid in addition to retirement bonus for exceptional length of employment.
    CUR_DATE = dt.now()  # Can be changed to fiscal year-end date if required.

    # Uses employee tenure to calculate standard, longevity and retention bonuses where applicable.
    def bonus(empYears):
        lonBonus = 0
        addBonus = 0
        if 2 <= empYears < 8:
            lonBonus = STANDARD_BONUS
        elif empYears >= 8:
            lonBonus = LON_BONUS * empYears
        if 8 < empYears <= 20:
            if empYears % 5 == 0:
                for year in range(9, int(empYears)):
                    addBonus = empYears * 10
        elif empYears > 20:
            lonBonus = LON_BONUS * SERVICE_CAP
            addBonus = SERVICE_CAP * 10
        return [lonBonus, addBonus]

    # Calculates retirement bonus where applicable
    def retirementBonus(empYears):
        retireBonus = RETIRE_BONUS * empYears
        tenureBonus = 0
        if empYears >= 10:
            tenureBonus = TENURE_BONUS
        return retireBonus, tenureBonus

    # Prevents empty user inputs.
    def blank(x):
        if x == "":
            return True
        else:
            return False

    # Gather required user information. NOTE: Create a function for date validation?
    while True:
        print("")
        print("NL Chocolate Company Year-End Bonus Calculator")
        while True:
            firstName = input("Employee first name: ")
            if blank(firstName) == False:
                break
        while True:
            lastName = input("Employee last name: ")
            if blank(lastName) == False:
                break
        while True:
            phoneNum = input("Employee 10-digit phone number [numbers only]: ")
            if blank(phoneNum) == False:
                try:
                    if len(phoneNum) == 10:
                        try:
                            phoneNum = int(phoneNum)
                            break
                        except:
                            print("Phone number not recognized.")
                except:
                    print("Phone number not recognized.")
        while True:
            try:
                startDay = input("Employee start date as YYYY-MM-DD: ")
                startDay = dt.strptime(startDay, "%Y-%m-%d")
            except:
                print("Date not valid or format not recognized.")
            else:
                break
        while True:
            try:
                birthDay = input("Employee birthday as YYYY-MM-DD: ")
                birthDay = dt.strptime(birthDay, "%Y-%m-%d")
            except:
                print("Date not valid or format not recognized. ")
            else:
                break
        break

    # Calculate employee age and tenure and format display values.
    empYears = CUR_DATE - startDay
    empYears = int(empYears.days / 365.2425)
    curAge = CUR_DATE - birthDay
    curAge = curAge.days / 365.2425
    if curAge < 65:
        bonus = bonus(empYears)
        retireCheck = False
    elif curAge >= 65:
        bonus = retirementBonus(empYears)
        retireCheck = True
    bonus1 = "${:.2f}".format(bonus[0])
    bonus2 = "${:.2f}".format(bonus[1])
    name = firstName + " " + lastName

    # Printout for user display.
    print("")
    print("             NL Chocolate Company")
    print("          Year End Bonus Calculator")
    print("")
    print("Employee:  {:>39}".format(name))
    print("Contact: {:>41}".format(phoneNum))
    print("Birthdate:                              {}".format(dt.date(birthDay)))
    print("Start date:                             {}".format(dt.date(startDay)))
    print("Years worked: {:>36}".format(empYears))
    print("")
    if retireCheck == False:
        if int(bonus[0]) <= 350:
            bonus2 = ""
            print("Standard Bonus:")
        else:
            print("Longevity Bonus:                  Retention Bonus:")
    if retireCheck == True:
        print("Retirement Bonus:               Recognition Bonus:")
    print("{}{:>42}".format(bonus1, bonus2))


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


# Main menu/program
main()
while True:
    userChoice = input("   Enter Choice (1-5): ")
    if userChoice == "":
        print("Entry cannot be blank.")
    elif userChoice.isnumeric() == False:
        print("Entry must be a number.")
    elif int(userChoice) > 5:
        print("Entry not recognized.")
    elif int(userChoice) == 0:
        print("Entry not recognized.")
    elif userChoice == "1":
        travelClaim()
        print()
        Key = input("Press any key to continue: ")
        print()
        main()
    elif userChoice == "2":
        fizzbuzz()
        print()
        Key = input("Press any key to continue: ")
        print()
        main()
    elif userChoice == "3":
        strDate()
        print()
        Key = input("Press any key to continue: ")
        print()
        main()
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
                    Claims.append(Jan)
                    break
            while True:
                try:
                    Feb = float(input("Enter the Total Sales For February: "))
                except:
                    print("February must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Feb)
                    break
            while True:
                try:
                    Mar = float(input("Enter the Total Sales For March: "))
                except:
                    print("March must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Mar)
                    break
            while True:
                try:
                    Apr = float(input("Enter the Total Sales For April: "))
                except:
                    print("April must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Apr)
                    break
            while True:
                try:
                    May = float(input("Enter the Total Sales For May: "))
                except:
                    print("May must have a valid number entry please - re-enter.")
                else:
                    Claims.append(May)
                    break
            while True:
                try:
                    Jun = float(input("Enter the Total Sales For June: "))
                except:
                    print("June must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Jun)
                    break
            while True:
                try:
                    Jul = float(input("Enter the Total Sales For July: "))
                except:
                    print("July must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Jul)
                    break
            while True:
                try:
                    Aug = float(input("Enter the Total Sales For August: "))
                except:
                    print("August must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Aug)
                    break
            while True:
                try:
                    Sep = float(input("Enter the Total Sales For September: "))
                except:
                    print("September must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Sep)
                    break
            while True:
                try:
                    Oct = float(input("Enter the Total Sales For October: "))
                except:
                    print("October cannot be blank.")
                else:
                    Claims.append(Oct)
                    break
            while True:
                try:
                    Nov = float(input("Enter the Total Sales For November: "))
                except:
                    print("November must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Nov)
                    break
            while True:
                try:
                    Dec = float(input("Enter the Total Sales For December: "))
                except:
                    print("December must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Dec)
                    break
            break

        Graph()
        print()
        Key = input("Press any key to continue: ")
        print()
        main()
    elif userChoice == "5":
        quit()
    else:
        print("Try again?")
