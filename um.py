import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Using \b to ensure "um" is a whole word, case-insensitive
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
