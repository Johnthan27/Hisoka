# Odd/Even Number Check
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Age Calculation Program
age = int(input("What is your current age? "))
remaining_years = 90 - age
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
