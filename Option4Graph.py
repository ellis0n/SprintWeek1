# A Program to display a graph of the NL Chocolate Company Total Travel Claims

# Written by Mark Hannem on February 26th

# Program Edited on Feb 27th, 28th and March 1st

# Import matplotlib for Graph functions
import matplotlib.pyplot as plt


def Graph():
    # Function for Graphing Total Claims
    Mths = ["Jan", "Feb", "Mar", "Apr'", "May", "June", "July", "Aug",
            "Sept", "Oct", "Nov", "Dec"]

    # Defining the size of the graph
    fig, ax = plt.subplots(figsize=(12, 8))

    # Formatting X/Y-axis, Titles and Graph Labels
    xaxis = Mths
    yaxis = Claims

    ax.plot(xaxis, yaxis, color="cyan", marker="o")

    plt.xlabel("Months", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.ylabel("Monthly Claims Total\n(dollars,$)", fontdict={'fontsize': 10, 'fontweight': 3, 'color': 'Crimson'})
    plt.setp(ax.get_xticklabels(), rotation=45)

    plt.title("NL Chocolate Company\nSales Totals Per Month", fontdict={'fontsize': 15,
                                                                        'fontweight': 5, 'color': 'darkgoldenrod'})
    plt.grid(True)

    plt.show()


# Main Program For Option 4: Total Claims
Claims = []
while True:
    print("Input Your Monthly Claims Total Below")
    print()

    while True:
        try:
            Jan = float(input("Enter the Total Claims For January: "))
        except:
            print("January claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Jan)
            break
    while True:
        try:
            Feb = float(input("Enter the Total Claims For February: "))
        except:
            print("February claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Feb)
            break
    while True:
        try:
            Mar = float(input("Enter the Total Claims For March: "))
        except:
            print("March claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Mar)
            break
    while True:
        try:
            Apr = float(input("Enter the Total Claims For April: "))
        except:
            print("April claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Apr)
            break
    while True:
        try:
            May = float(input("Enter the Total Claims For May: "))
        except:
            print("May claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(May)
            break
    while True:
        try:
            Jun = float(input("Enter the Total Claims For June: "))
        except:
            print("June claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Jun)
            break
    while True:
        try:
            Jul = float(input("Enter the Total Claims For July: "))
        except:
            print("July claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Jul)
            break
    while True:
        try:
            Aug = float(input("Enter the Total Claims For August: "))
        except:
            print("August claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Aug)
            break
    while True:
        try:
            Sep = float(input("Enter the Total Claims For September: "))
        except:
            print("September claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Sep)
            break
    while True:
        try:
            Oct = float(input("Enter the Total Claims For October: "))
        except:
            print("October claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Oct)
            break
    while True:
        try:
            Nov = float(input("Enter the Total Claims For November: "))
        except:
            print("November claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Nov)
            break
    while True:
        try:
            Dec = float(input("Enter the Total Claims For December: "))
        except:
            print("December claims must have a valid number entry please - re-enter.")
        else:
            Claims.append(Dec)
            break
    break

Graph()
