
# Question 3:
# Calculate Compound Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

compound_interest = principal * (1 + rate/100)**time - principal

compound_interest = round(compound_interest, 2)

print("Compound Interest is:", compound_interest) 
