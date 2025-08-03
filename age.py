
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - \
        ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    print("📆 Age Calculator")
    dob_input = input("Enter your birth date (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        age = calculate_age(dob)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()