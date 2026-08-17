# Question 7:
# Distribute Items Equally - You have n candies and k students.
# Write a program to find:
# how many candies each student gets
# how many are left

n = int(input("Enter the number of candies: "))
k = int(input("Enter the number of students: "))

candies_per_student = n // k
candies_left = n % k

print("Each student gets:", candies_per_student, "candies")
print("Candies left:", candies_left)