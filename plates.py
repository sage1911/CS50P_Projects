def is_valid(s):
    # Check length constraint
    if len(s) < 2 or len(s) > 6:
        return False

    # Check first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check if numbers are only at the end
    num_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and num_started is False:  # First number cannot be '0'
                return False
            num_started = True
        elif num_started:  # A letter after a number is not allowed
            return False

    # Check only letters and numbers (no special characters)
    if not s.isalnum():
        return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
