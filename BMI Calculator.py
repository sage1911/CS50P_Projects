def main():
    weight = float(input("Whats your weight in kgs?: "))
    height = float(input("What's your height in metres?: "))

    bmi = bmi_calculator(weight, height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"BMI: {bmi: .2f}")        
    print(f"Category: {category}")


def bmi_calculator(weight, height):
    return weight / (height ** 2)

main()        
