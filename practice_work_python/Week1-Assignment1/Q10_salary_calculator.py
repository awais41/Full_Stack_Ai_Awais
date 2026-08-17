# Question 10:
# Salary Calculator
# Input basic salary. 
# Calculate:
# HRA = 20% of basic
# DA = 15% of basic
# Total Salary = Basic + HRA + DA

basic_salary = float(input("Enter the basic salary: "))

hra = 0.20 * basic_salary
da = 0.15 * basic_salary
total_salary = basic_salary + hra + da

print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)
