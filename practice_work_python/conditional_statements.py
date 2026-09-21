marks = int(input("Enter student marks : "))

if(marks <=0 or  marks > 100 ):
    print("Invalid Marks")
else:
 if(marks>=90 ):
    grade = "A+"
 elif(marks>=80 ):
    grade = "A"
 elif(marks>=70 ):
    grade = "B"
 elif(marks>=60 ):
    grade = "C"
 elif(marks>=50):
    grade = "D"
 else:
    grade = "F"
    print("Student is failed : ")
 print("Grade:", grade)

