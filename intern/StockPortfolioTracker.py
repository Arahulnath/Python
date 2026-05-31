# predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))
    value = stock_prices[stock] * quantity
    total_investment += value

    print(f"{stock} value: {value}")

print("\nTotal Investment Value:", total_investment)

# optional file saving
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total_investment}")

print("Saved to portfolio.txt")