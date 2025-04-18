def main():
    distance_km = float(input("What is the distance in KM?: "))
    print(f"Distance in Miles is:{km_to_miles(distance_km): .2f}")

def km_to_miles(distance_km):
    multiply = 0.621371
    return multiply * distance_km

main()

