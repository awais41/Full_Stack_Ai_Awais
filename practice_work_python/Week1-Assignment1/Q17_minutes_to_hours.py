# Question 17:
# Convert Minutes to Hours and Minutes
# Input number of minutes and convert to hours and remaining minutes.
# Example: 130 minutes -> 2 hours 10 minutes

total_minutes = int(input("Enter number of minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(hours, "hours", remaining_minutes, "minutes")
