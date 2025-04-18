import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.match(pattern, ip)    

    if not match:
        return False
    
    return all(0 <= int(octet) <= 255 for octet in match.groups())

if __name__ == "__main__":
    main()
