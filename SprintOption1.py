# Program fro NL Chocolate Company to process salesperson travel claims when they return from a business trip

# import needed functions
from datetime import datetime
from datetime import timedelta

# Define constants
DAILY_RATE = 85.00  # This value is a daily rate to be multiplied by total days spent on business trip
MILEAGE_OWN = .17  # This value multiplied by the total kilometers driven only if the employee used their own car
MILEAGE_RENT = 65.00  # This value multiplied by the total days spent on business trip if employee used a rental vehicle
HST_RATE = .15  # Represents taxes to be multiplied by the per diem amount later on
EXEC_RATE = 45.00  # Amount multiplied by the NumDays if employee claim type is "executive", then is added to the bonus
TRAVEL_RATE = .04  # Amount multiplied by TotKilos if employee travelled >1000km using their own car and added to bonus
STAY_BONUS = 100.00  # Amount added to the bonus if employee was on trip longer than 3 days
HOLIDAY_BONUS = 50.00  # Amount to be multiplied by NumDays and added to bonus if Dec 15 < TripStartDate < Dec 22

# Define necessary functions


def blank(x):  # Prevents empty user inputs
    if x == "":  # x is whatever input needs to be checked for a null string
        return True  # if x is a null string, return boolean "True"
    else:
        return False  # if x is not a null string, return boolean "False"


# Define any subsets needed for validations
allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-"


# Acquire necessary inputs from user with validations withing a global "while True" loop
while True:
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
            TripStart = input("Enter the start date of the business trip (YYYY/MM/DD): ")
            TripStartDate = datetime.strptime(TripStart, "%Y/%m/%d")
        except:
            print("Not a valid date - please re-enter.")
        else:
            break

    while True:
        try:
            TripEnd = input("Enter the end date of the business trip (YYYY/MM/DD): ")
            TripEndDate = datetime.strptime(TripEnd, "%Y/%m/%d")
        except:
            print("Not a valid date - please re-enter.")
        else:
            break

    while True:
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

    # Begin displaying calculated outputs using headings and basic formatting
    PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
    MileageDsp = "${:,.2f}".format(Mileage)
    BonusDsp = "${:,.2f}".format(Bonus)
    ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
    HSTDsp = "${:,.2f}".format(HST)
    ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)

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
