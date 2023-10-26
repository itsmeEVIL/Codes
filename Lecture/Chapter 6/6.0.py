"""
Pseudocode
1. START
2. Declare variable number
3. Prompt & Get number
4. If number % 2 and number % 3
    4.1 Display number, "is divisible by 2 and 3!"
5 If number % 2
    5.1 Display number, "is divisible by 2!"
6. If number % 3
    6.1 Display number, "is divisible by 3!"
7. Else
    6.1 Display number, "is not divisible by 2 or 3!"
8. END
"""





























number = int(input("Enter an interger: "))

if number % 2 == 0 and number % 3 == 0:
  print(f"{number} is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
  print(f"{number} is divisible by 2 or 3")
