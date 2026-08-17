# Question 14:
# Percentage of Correct Answers
# Input total questions and correct answers, and calculate the percentage score.

total_questions = int(input("Enter the total number of questions: "))
correct_answers = int(input("Enter the number of correct answers: "))

percentage = (correct_answers / total_questions) * 100
percentage = round(percentage, 2)

print("Percentage of correct answers:", percentage)