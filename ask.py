def main():
    """Simple program for illustrative purposes"""
    age = ask_user_age()
    print_age(age)


def ask_user_age():
    """Return user input"""
    age = input("What is your age in years? ")
    return age


def print_age(age):
    """Print full sentence"""
    age_in_months = age * 12
    print(f"You are {age_in_months} months old.")

print('inside ask.py')
print(__name__)
if __name__ == "__main__":
    print('inside ask.py and inside if')
    main()

