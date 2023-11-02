month = str(input("Enter the month name: ").lower())

if month == "september" or month == "april" or month == "june" or month == "november":
    numDays = 30
elif month == "february":
    leapYear = str(input("Is it a leap year?(Y/n)").lower())
    if leapYear == "y" or leapYear == "yes":
        numDays = 29
    elif leapYear == "n" or leapYear == "no":
        numDays = 28
    else:
        print("Not a valid answer.")
        exit()
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    numDays = 31
else:
    print("Not a valid month.")
    exit()

i = 1
apiReading = 0
while i <= numDays:
    api = int(input(f"Enter the api readings for day {i}: "))

    if 0 <= apiReading <= 50:
        status = "Good"
    elif 51 <= apiReading <= 100:
        status = "Moderate"
    elif 101 <= apiReading <= 200:
        status = "Unhealthy"
    elif 201 <= apiReading <= 300:
        status = "Very Unhealthy"
    else:
        status = "Hazardous"

    print(
        f"The API readings for day {i} is {apiReading} and the status is {status}."
    )
    i += 1
