# Question 15:
# Speed, Distance, and Time
# Input distance and time, and calculate speed.

distance = float(input("Enter the distance (in km): "))
time = float(input("Enter the time (in hours): "))

speed = distance / time
speed = round(speed, 2)

print("Speed is:", speed, "km/h")