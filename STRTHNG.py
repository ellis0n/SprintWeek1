# This function was written for the NL Chocolate Company.
# Calculates and determines employee eligibility to year-end bonus pay-outs.
# Bonuses included: standard, longevity, retention, retirement and tenure.
# Please see Technical Manual for further clarification on company policy.
# Written by Glen May on February 27, 2022.

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
    if empYears >= 20:
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
    while True:
        firstName = "Joanie"  # input("Employee first name: ")
        if blank(firstName) == False:
            break
    while True:
        lastName = "Whitten"  # input("Employee last name: ")
        if blank(lastName) == False:
            break
    while True:
        phoneNum = "7097287272"  # input("Employee 10-digit phone number [numbers only]: ")
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
            startDay = "2000-02-28"  # input("Employee start date as YYYY-MM-DD: ")
            startDay = dt.strptime(startDay, "%Y-%m-%d")
        except:
            print("Date not valid or format not recognized.")
        else:
            break
    while True:
        try:
            birthDay = "1954-02-28"  # input("Employee birthday as YYYY-MM-DD: ")
            birthDay = dt.strptime(birthDay, "%Y-%m-%d")
        except:
            print("Date not valid or format not recognized. ")
        else:
            break
    break

# Calculate employee age and tenure.
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
