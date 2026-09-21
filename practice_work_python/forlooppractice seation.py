# QS1  


for i in range(1,6):
    print("Hello, World!")
 
#  QS2 
 
num = int(input("Enter a number:"))
for i in range(1, num + 1):
    print(i) 
    if(i == 5): 
        break
 
print("Loop ended") 
 

#  Qs3 

for i in range(1, 6):
    print(i)

# reverse counting using for loop 
for i in range(5, 0, -1):
    print(i)
 

# QS4
#  sum of 5 natural numbers using for loop  
num = int(input("Enter a number:"))
sum = 0 
for i in range(1, num , 1):
    sum = sum + i 
    if(i == 5):
        break
print("The sum of the first", num, "natural numbers is:", sum)

# QS5
# print the table of any number with user input using for loop 

num = int(input("Enter a number:"))
for i in range(1,11): 
    print(num, "x", i, "=",num*i) 


# QS6
# print first 5 natural numbers using for loop
for i in range(1,6):
    print(i)

# # QS7
# # factorial of a number using for loop 
num = int(input("Enter an number")) 
fact = 1
for i in range(1, num +1):
    fact *= i
    print("The factorial of", num , "is",fact)
  


num = int(input("Enter a number: "))
fact = 1 
for i in range(1,num +1):
    
    fact =  fact* i
    print("The factorial of ", num, "is",fact)