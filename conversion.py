##
# conversion.py
# Sam Fernyhough
# Program that asks the user what type of units they want to convert
# 17/03/2021


# Knots to km
def knots_km(knots):
    """
    Accepts knots as a float
    Returns kmph as a float
    """
    CONVERSION = 1.852
    return knots * CONVERSION


# Feet to cm
def feet_cm(feet):
    """
    Accepts feet as a float
    Returns cm as a float
    """
    CONVERSION = 30.48
    return feet * CONVERSION


# Inches to cm
def inches_cm(inches):
    """
    Accepts inches as a float
    Returns cm as a float
    """
    CONVERSION = 2.54
    return inches * CONVERSION


# Cups to grams
def cups_grams(cups):
    """
    Accepts cups as a float
    Returns grams as a integer
    """
    CONVERSION = 130
    return int(cups * CONVERSION)


def menu():
    """
    Print out the menu
    Get choice from user
    """

    # Define menu choices
    MENU = [0, 1, 2, 3, 4]

    choice = 1

# Loop program until user decides to quit
    while choice != 0:
        # Display menu
        print("Welcome to my conversion programme.")
        print("1. Knots to km/h\n" +
              "2. Feet to cm\n" +
              "3. Inches to cm\n" +
              "4. Cups to grams\n" +
              "0. Quit\n")

        # Get input choice from user
        try:
            choice = int(input("Enter option: "))
        except:
            print("Please enter a valid option")

        if choice == 0:
            print("Thanks for using my programme , goodbye")
        else:
            check_input(choice)


def check_input(choice):
    """
    Accepts the user choice
    calls corresponding function
    """

    # Ask the user for unit
    while True:
        try:
            unit = float(input("Enter a unit ot convert: "))
            break
        except:
            print("Enter a valid unit of measurement")

    # Select from menu
    if choice == 1:
        print("{} knots is {:.2f} kmh".format(unit, knots_km(unit)))
    elif choice == 2:
        print("{} feet is {:.2f} cm".format(unit, feet_cm(unit)))
    elif choice == 3:
        print("{} inches is {:.2f} cm".format(unit, inches_cm(unit)))
    elif choice == 4:
        print("{} cups is {} grams".format(unit, cups_grams(unit)))
    else:
        print("Not valid input")


# Main routine
if __name__ == "__main__":
    menu()
