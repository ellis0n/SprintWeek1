# Group 22A3 - Sprint Week Program
# Written by Glen May, Mark Hannem & Jacob Eagles
# Written between February 25th 2022 and March 6th 2022
# This program offers several options for

# Common modules between functions
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


# Prevents empty user inputs or null strings.
def blank(x):  # Accepts any variable
    if x == "":
        return True
    else:
        return False


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


def travelClaim():
    # Validation subsets
    allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-."
    # Define constants
    DAILY_RATE = 85.00  # This value is a daily rate to be multiplied by total days spent on business trip
    MILEAGE_OWN = .17  # This value multiplied by the total kilometers driven only if the employee used their own car
    MILEAGE_RENT = 65.00  # This value multiplied by the total days spent on business trip if employee used a rental vehicle
    HST_RATE = .15  # Represents taxes to be multiplied by the per diem amount later on
    EXEC_RATE = 45.00  # Amount multiplied by the NumDays if employee claim type is "executive", then is added to the bonus
    TRAVEL_RATE = .04  # Amount multiplied by TotKilos if employee travelled >1000km using their own car and added to bonus
    STAY_BONUS = 100.00  # Amount added to the bonus if employee was on trip longer than 3 days
    HOLIDAY_BONUS = 50.00  # Amount to be multiplied by NumDays and added to bonus if Dec 15 < TripStartDate < Dec 22

    # Gather user inputs
    while True:
        print()
        print("NL Chocolate Company\nEmployee Travel Claim")
        print()
        while True:
            EmpNum = input("Enter the employee's employee number: ")
            if blank(EmpNum) == True:
                print("Employee number cannot be blank - please re-enter.")
            elif len(EmpNum) != 5:
                print("Employee number must be 5 characters - please re-enter.")
            elif EmpNum.isdigit() == False:
                print("Employee number contains invalid characters - please re-enter.")
            else:
                break
        while True:
            EmpFirst = input("Enter the employee's first name: ").title()
            if blank(EmpFirst) == True:
                print("Employee's first name cannot be blank - please re-enter.")
            elif set(EmpFirst).issubset(allowed_char) == False:
                print("Employee's first name contains invalid characters - please re-enter.")
            else:
                break
        while True:
            EmpLast = input("Enter the employee's last name: ").title()
            if blank(EmpLast) == True:
                print("Employee's last name cannot be blank - please re-enter.")
            elif set(EmpLast).issubset(allowed_char) == False:
                print("Employee's last name contains invalid characters - please re-enter.")
            else:
                break
        while True:
            City = input("Enter the city where the business trip was: ")
            if blank(City) == True:
                print("Trip city cannot be blank - please re-enter.")
            elif set(City).issubset(allowed_char) == False:
                print("Trip city contains invalid characters - please re-enter.")
            else:
                break
        while True:
            Country = input("Enter the country where the business trip was: ")
            if blank(Country) == True:
                print("Trip country cannot be blank - please re-enter.")
            elif set(Country).issubset(allowed_char) == False:
                print("Trip country contains invalid characters - please re-enter.")
            else:
                TripLoc = City + "," + " " + Country
                break
        while True:
            try:
                TripStart = input("Enter the start date of the business trip (YYYY-MM-DD): ")
                TripStartDate = datetime.strptime(TripStart, "%Y-%m-%d")
            except:
                print("Not a valid date - please re-enter.")
            else:
                break
        while True:
            try:
                TripEnd = input("Enter the end date of the business trip (YYYY-MM-DD): ")
                TripEndDate = datetime.strptime(TripEnd, "%Y-%m-%d")
            except:
                print("Not a valid date - please re-enter.")
            if TripEndDate > TripStartDate + timedelta(days=7):
                print("The trip end date cannot be more than 7 days after trip start date - please re-enter.")
            elif TripEndDate < TripStartDate:
                print("The trip end date cannot be before the trip start date - please re-enter.")
            else:
                NumDays = TripEndDate.day - TripStartDate.day
                break
        while True:
            OwnCar = input("Enter if the employee rented a vehicle or used their own (R / O): ").upper()
            if blank(OwnCar) == True:
                print("Must enter if employee rented a vehicle or used their own - please re-enter.")
            if OwnCar != "O" and OwnCar != "R":
                print("Invalid input - please re-enter.")
            elif OwnCar == "R":
                break
        while True:
            TotKilos = int(input("Enter the total number of kilometers travelled (must be < 2000km): "))
            if blank(TotKilos) == True:
                print("Total kilometers cannot be blank - please re-enter.")
            if TotKilos > 2000:
                print("Total kilometers cannot exceed 2000km - please re-enter.")
            else:
                break
        while True:
            ClaimType = input("Enter if the claim type is standard or executive (S / E): ").upper()
            if blank(ClaimType) == True:
                print("Claim type cannot be blank - please re-enter.")
            elif ClaimType != "S" and ClaimType != "E":
                print("Claim type must be \"S\" for standard or \"E\" for executive - please re-enter.")
            else:
                break

        # Perform calculations using inputted values and constants defined earlier
        PerDiemAmt = NumDays * DAILY_RATE
        Mileage = 0
        if OwnCar == "R":
            TotKilos = 0
        elif OwnCar == "O":
            Mileage = TotKilos * MILEAGE_OWN
        else:
            Mileage = NumDays * MILEAGE_RENT
        Bonus = 0
        if NumDays > 3:
            Bonus += STAY_BONUS
        elif TotKilos > 1000 and OwnCar == "O":
            Bonus += TotKilos * TRAVEL_RATE
        elif ClaimType == "E":
            Bonus += NumDays * EXEC_RATE
        elif TripStartDate.month == 12 and 15 < TripStartDate.day < 22:
            Bonus += NumDays * HOLIDAY_BONUS
        ClaimAmt = PerDiemAmt + Mileage + Bonus
        HST = PerDiemAmt * HST_RATE
        ClaimTotal = ClaimAmt + HST

        # Formatting dollar value amounts
        PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
        MileageDsp = "${:,.2f}".format(Mileage)
        BonusDsp = "${:,.2f}".format(Bonus)
        ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
        HSTDsp = "${:,.2f}".format(HST)
        ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)

        # Display outputs to user
        print()
        print("Employee Number:                         {}".format(EmpNum))
        print("Employee Name:                           {}".format(EmpFirst + " " + EmpLast))
        print("Trip Location:                           {}".format(TripLoc))
        print("Trip Start Date:                         {}".format(TripStartDate))
        print("Trip End Date:                           {}".format(TripEndDate))
        print("Number of Days Spent on Trip:            {}".format(NumDays))
        print("Did Employee Rent or Use Own Vehicle?:   {}".format(OwnCar))
        if OwnCar == "O":
            print("Total Kilometers Travelled:              {}km".format(TotKilos))
        print("Employee Travel Claim Type:              {}".format(ClaimType))
        print("Per Diem Amount:                         {}".format(PerDiemAmtDsp))
        print("Mileage Amount:                          {}".format(MileageDsp))
        print("Bonus Amount:                            {}".format(BonusDsp))
        print("HST:                                     {}".format(HSTDsp))
        print("Claim Total Amount:                      {}".format(ClaimTotalDsp))
        print()
        Continue = input("Would you like to process another claim? (Y / N): ").upper()
        if Continue == "N":
            break


# Function that solves the classic "FizzBuzz" interview question.
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


# Calculates and determines employee eligibility to year-end bonus pay-outs.
# Bonuses included: standard, longevity, retention, retirement and tenure.
# Please see Technical Manual for further clarification on company policy.
# Written by Glen May on February 27, 2022.
def strDate():

    STANDARD_BONUS = 350.00  # Payable to employees after 2 years of employment..
    LON_BONUS = 50.00  # Replaces the standard bonus at 8 years of employment. Paid per year of employment.
    SERVICE_CAP = 20  # Longevity bonus yearly multiplier limit.
    RETIRE_CAP = 65  # Company policy for mandatory retirement at age 65.
    RETIRE_BONUS = 100.00  # Replaces standard and longevity bonus and is paid on retirement.
    TENURE_BONUS = 200.00  # Paid in addition to retirement bonus for exceptional length of employment.
    CUR_DATE = datetime.now()  # Can be changed to fiscal year-end date if required.

    # Uses employee tenure to calculate standard, longevity and retention bonuses where applicable.
    def bonus(empYears): # Passes through employee length of service
        lonBonus = 0
        retBonus = 0
        if 2 <= empYears < 8:
            lonBonus = STANDARD_BONUS
        elif empYears >= 8:
            lonBonus = LON_BONUS * empYears
        if 8 < empYears <= 20:
            if empYears % 5 == 0:
                for year in range(9, int(empYears)):
                    retBonus = empYears * 10
        elif empYears > 20:
            lonBonus = LON_BONUS * SERVICE_CAP
            retBonus = SERVICE_CAP * 10
        return lonBonus, retBonus  # Outputs longevity bonuses and retention bonuses

    # Calculates retirement bonuses.
    def retirementBonus(empYears):  # Passes through employee length of service
        retireBonus = RETIRE_BONUS * empYears
        tenureBonus = 0
        if empYears >= 10:
            tenureBonus = TENURE_BONUS
        return retireBonus, tenureBonus  # Outputs retirement bonuses and tenure bonuses

    # Gather required user information.
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
                startDay = datetime.strptime(startDay, "%Y-%m-%d")
            except:
                print("Date not valid or format not recognized.")
            else:
                break
        while True:
            try:
                birthDay = input("Employee birthday as YYYY-MM-DD: ")
                birthDay = datetime.strptime(birthDay, "%Y-%m-%d")
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
    else:
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
    print("Birthdate:                              {}".format(datetime.date(birthDay)))
    print("Start date:                             {}".format(datetime.date(startDay)))
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


# Function that graphs total sales
def Graph():
    # Function for Graph
    Mths = ["Jan", "Feb", "Mar", "Apr'", "May", "June", "July", "Aug",
            "Sept", "Oct", "Nov", "Dec"]
    # Formatting x/y-axis, titles and graph
    fig, ax = plt.subplots(figsize=(12, 8)) # Define Plot Space
    xaxis = Mths
    yaxis = Claims
    ax.plot(xaxis, yaxis, color="cyan", marker="o")
    plt.xlabel("Months", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.ylabel("Monthly Totals\n(dollars,$)", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.title("NL Chocolate Company\nSales Totals Per Month", fontdict={'fontsize': 15,
                                                                        'fontweight': 5, 'color': 'darkgoldenrod'})
    plt.grid(True)
    plt.show()
    return plt.show()


# Main Program
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
        Claims = []
        while True:
            print("Input Your Monthly Sales Total Below")
            print()
            while True:
                try:
                    Jan = float(input("Enter the Total Travel Claims For January: "))
                except:
                    print("January must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Jan)
                    break
            while True:
                try:
                    Feb = float(input("Enter the Total Travel Claims For February: "))
                except:
                    print("February must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Feb)
                    break
            while True:
                try:
                    Mar = float(input("Enter the Total Travel Claims For March: "))
                except:
                    print("March must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Mar)
                    break
            while True:
                try:
                    Apr = float(input("Enter the Total Travel Claims For April: "))
                except:
                    print("April must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Apr)
                    break
            while True:
                try:
                    May = float(input("Enter the Total Travel Claims For May: "))
                except:
                    print("May must have a valid number entry please - re-enter.")
                else:
                    Claims.append(May)
                    break
            while True:
                try:
                    Jun = float(input("Enter the Total Travel Claims For June: "))
                except:
                    print("June must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Jun)
                    break
            while True:
                try:
                    Jul = float(input("Enter the Total Travel Claims For July: "))
                except:
                    print("July must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Jul)
                    break
            while True:
                try:
                    Aug = float(input("Enter the Total Travel Claims For August: "))
                except:
                    print("August must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Aug)
                    break
            while True:
                try:
                    Sep = float(input("Enter the Total Travel Claims For September: "))
                except:
                    print("September must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Sep)
                    break
            while True:
                try:
                    Oct = float(input("Enter the Total Travel Claims For October: "))
                except:
                    print("October cannot be blank.")
                else:
                    Claims.append(Oct)
                    break
            while True:
                try:
                    Nov = float(input("Enter the Total Travel Claims For November: "))
                except:
                    print("November must have a valid number entry please - re-enter.")
                else:
                    Claims.append(Nov)
                    break
            while True:
                try:
                    Dec = float(input("Enter the Total Travel Claims For December: "))
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
