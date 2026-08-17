# Question 12:
# Currency Converter (USD to PKR)
# Input amount in USD. Convert using a fixed exchange rate.

usd_amount = float(input("Enter amount in USD: "))

# fixed exchange rate (approximate, can be changed as needed)
exchange_rate = 278

pkr_amount = usd_amount * exchange_rate

print("Amount in PKR :", pkr_amount)
