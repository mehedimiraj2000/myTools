from datetime import datetime
today = datetime.now()
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day
if days < 0:
    months -= 1
    days += (birthdate.replace(year=today.year, month=today.month) - 
              birthdate.replace(year=today.year, month=today.month - 1)).days

if months < 0:
    years -= 1
    months += 12
print(f"Age: {years} years, {months} months, and {days} days")
