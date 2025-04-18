def main():
    dollars = dollars_to_float(input("How much was the meal?: "))
    percentage = percentage_to_float(input("How much would you like to tip?: "))

    tip = dollars * percentage 
    print(f"Leave ${tip: .2f}")

def dollars_to_float(d):
    return float(d.replace("$", ""))  

def percentage_to_float(p):
    return float(p.replace("%", "")) / 100

main()