# Question 8:
# Calculate Profit or Loss
# Input cost price and selling price. Display either:
# Profit and amount, or
# Loss and amount, or
# No Profit No Loss

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No Profit No Loss")
    