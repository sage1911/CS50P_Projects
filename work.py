import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match various formats
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    h1, m1, p1, h2, m2, p2 = match.groups()
    
    # Default minutes to 00 if not provided
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)
    
    # Validate hours and minutes
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12 and 0 <= m1 < 60 and 0 <= m2 < 60):
        raise ValueError("Invalid time values")
    
    # Convert to 24-hour format
    h1 = (h1 % 12) + (12 if p1 == "PM" else 0)
    h2 = (h2 % 12) + (12 if p2 == "PM" else 0)
    
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == "__main__":
    main()
