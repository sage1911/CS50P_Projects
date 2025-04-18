import sys
import requests

def get_price_per_bitcoin():
    
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUSD"])


    except requests.RequestException:
        sys.exit("Error: Failed to fetch price. Please try again later.")

def main():
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid input. Please enter a number.")

    price_per_bitcoin = get_price_per_bitcoin()
    total_cost = bitcoins * price_per_bitcoin
    print(f"Total cost: ${total_cost:.4f}")


if __name__ == "__main__":
    main()