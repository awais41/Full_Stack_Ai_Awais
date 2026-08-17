# Python Loops Practice
# Week 1 - practicing for loop, while loop, nested loops

# Q1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("-----")

# Q2: Print even numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)

print("-----")

# Q3: Sum of first n natural numbers (using while loop)
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of first", n, "numbers is:", total)

print("-----")

# Q4: Print multiplication table of a number
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("-----")

# Q5: Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Liftoff!")

print("-----")

# Q6: Find factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is:", fact)

print("-----")

# Q7: Print a simple pattern (right angle triangle of stars)
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("-----")

# Q8: Check if a number is prime (loop based)
num = 29
is_prime = True
if num < 2:
    is_prime = False
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("-----")

# Q9: Reverse a string using a loop
text = "hello world"
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print("Reversed:", reversed_text)

print("-----")

# Q10: Loop through a list and find the largest number
numbers = [4, 9, 2, 17, 5, 23, 1]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest number is:", largest)
