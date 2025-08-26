rates = {"USD": 1.0, "INR": 83.0, "EUR": 0.92, "GBP": 0.78, "JPY": 146.5}

def convert(amount, source, target):
    usd = amount / rates[source]
    return usd * rates[target]

amount = float(input("Enter amount: "))
source = input("From Currency (USD/INR/EUR/GBP/JPY): ").upper()
target = input("To Currency (USD/INR/EUR/GBP/JPY): ").upper()

if source in rates and target in rates:
    result = convert(amount, source, target)
    print(f"{amount} {source} = {result:.2f} {target}")
else:
    print("Invalid currency code!")
