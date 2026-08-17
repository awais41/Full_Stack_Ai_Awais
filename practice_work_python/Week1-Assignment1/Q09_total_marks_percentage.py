# Question 9:
# Total Marks and Percentage
# Input marks of 5 subjects.
# Print:
#       Total marks
#        Percentage
#        Average

subject1 = float(input("Enter marks of subject 1: "))
subject2 = float(input("Enter marks of subject 2: "))
subject3 = float(input("Enter marks of subject 3: "))
subject4 = float(input("Enter marks of subject 4: "))
subject5 = float(input("Enter marks of subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# assuming each subject is out of 100, so total is out of 500

percentage = (total_marks / 500) * 100
average = total_marks / 5

percentage = round(percentage, 2)
average = round(average, 2)

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Average:", average)