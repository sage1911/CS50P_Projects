def main():
    fraction = fraction_to_float(input("What is fuel fraction?: "))
    percent = fraction * 100

    if percent >= 99:
        print("Full")
    elif percent <=1:
        print("empty")
    else:
        print(f"{round(percent)}%")

def fraction_to_float(fraction):
    numerator, denominator = map(int, fraction.split("/"))        
    return numerator/denominator

main()
