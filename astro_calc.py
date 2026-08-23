# Constants for speed of light calculations (in miles)
MILES_PER_LIGHT_SECOND = 186282
MILES_PER_LIGHT_MINUTE = MILES_PER_LIGHT_SECOND * 60
MILES_PER_LIGHT_HOUR   = MILES_PER_LIGHT_MINUTE * 60
MILES_PER_LIGHT_DAY    = MILES_PER_LIGHT_HOUR * 24
MILES_PER_LIGHT_WEEK   = MILES_PER_LIGHT_DAY * 7
MILES_PER_LIGHT_MONTH  = MILES_PER_LIGHT_DAY * (365.25 / 12)  # Average month length
MILES_PER_LIGHT_YEAR   = MILES_PER_LIGHT_DAY * 365.25

def light_minutes_to_miles(minutes):
    return minutes * MILES_PER_LIGHT_MINUTE

def light_hours_to_miles(hours):
    return hours * MILES_PER_LIGHT_HOUR

def light_days_to_miles(days):
    return days * MILES_PER_LIGHT_DAY

def light_weeks_to_miles(weeks):
    return weeks * MILES_PER_LIGHT_WEEK

def light_months_to_miles(months):
    return months * MILES_PER_LIGHT_MONTH

def light_years_to_miles(years):
    return years * MILES_PER_LIGHT_YEAR

print("--- Astrophysics Distance Converter ---")
print("1. Light-Minutes (e.g., Sun, Inner Planets)")
print("2. Light-Hours   (e.g., Saturn, Pluto, Voyager 1)")
print("3. Light-Days    (e.g., Oort Cloud edge)")
print("4. Light-Weeks   (e.g., Inner Oort Cloud boundary)")
print("5. Light-Months  (e.g., Outer Oort Cloud boundary)")
print("6. Light-Years   (e.g., Stars and Galaxies)")

choice = input("\nSelect conversion type (1-6): ")

if choice == "1":
    val = float(input("Enter distance in Light-Minutes: "))
    print(f"\n[+] {val} Light-Minutes = {light_minutes_to_miles(val):,.2f} Miles")

elif choice == "2":
    val = float(input("Enter distance in Light-Hours: "))
    print(f"\n[+] {val} Light-Hours = {light_hours_to_miles(val):,.2f} Miles")

elif choice == "3":
    val = float(input("Enter distance in Light-Days: "))
    print(f"\n[+] {val} Light-Days = {light_days_to_miles(val):,.2f} Miles")

elif choice == "4":
    val = float(input("Enter distance in Light-Weeks: "))
    print(f"\n[+] {val} Light-Weeks = {light_weeks_to_miles(val):,.2f} Miles")

elif choice == "5":
    val = float(input("Enter distance in Light-Months: "))
    print(f"\n[+] {val} Light-Months = {light_months_to_miles(val):,.2f} Miles")

elif choice == "6":
    val = float(input("Enter distance in Light-Years: "))
    print(f"\n[+] {val} Light-Years = {light_years_to_miles(val):,.2f} Miles")

else:
    print("\n[-] Invalid selection. Please run the script again.")
