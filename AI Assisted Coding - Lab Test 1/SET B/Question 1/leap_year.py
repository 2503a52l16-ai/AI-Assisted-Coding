# Program to check if a given year is a leap year

# Accept year input from user and strip extra spaces/dots
year_input = input("Enter a year: ").strip().replace(".", "")

# Convert to integer
year = int(year_input)

# Check for leap year conditions
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
