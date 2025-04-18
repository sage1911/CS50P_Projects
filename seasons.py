from datetime import date
import sys
import inflect

def main():
    birth_date = get_birth_date()
    minutes = calculate_minutes(birth_date)
    print(convert_to_words(minutes))

def get_birth_date():
    user_input = input("Date of Birth (YYYY-MM-DD): ")
    try:
        return date.fromisoformat(user_input)
    except ValueError:
        sys.exit("Invalid date format")

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60  # Convert days to minutes

def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")  # Remove "and"
    return words.capitalize() + " minutes"

if __name__ == "__main__":
    main()
