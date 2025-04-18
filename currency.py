def main():
    user_input = float(input("How much in INR?: "))

    print(f"Currency in dollars is: ${inr_to_usd(user_input): .2f}")

def inr_to_usd(inr_amount):
        exchange_rate = 83
        return inr_amount / exchange_rate
    
main()    
    
