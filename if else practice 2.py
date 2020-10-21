#this iss practice 2

'''
5.
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

'''
marks=int(input("Enter your total marks:"))
if marks < 25 :
 print("Your grade is f,fail")
elif marks >=25 and marks < 45:
 print("your grade is E , pass by gracing")
elif marks >=45 and marks < 50:
 print("your grade is D, below average marks")
elif marks >=50 and marks < 60 :
 print("your grade is c, average marks")
elif marks >=60 and marks < 80:
 print("Your grade is B, nice marks")
elif marks >= 80 and marks <= 100:
 print("Your grade is A , very nice great marks")
else:
 print("The marks should be between 1 to 100")
'''
6.
Take input of age of 3 people by user and determine oldest and youngest among them.
'''
usr1=int(input("Enter the first age:"))
usr2=int(input("Enter the second age:"))
usr3=int(input("Enter the third age:"))

if usr1 >= usr2 and usr1 >= usr3:
 print(usr1 ,"is the oldest")
elif usr2 >= usr1 and usr2 >= usr3:
 print(usr2,"is the oldest")
elif usr3 >= usr2 and usr3 >= usr1 :
 print(usr3,"is the oldest")
else:
 print("all are equal")
'''
8.
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

'''
no_of_classheld=int(input("Enter the no of classes held:"))

no_of_classattended = int(input("Enter the no of classes you attended:"))

attendence = (no_of_classattended * 100) / no_of_classheld

print("your attendence is ",attendence )

medical_cause=str(input("do you have any medical cause:"))

if medical_cause == "y":

 print("please take care do not give the exam")

else:

 if attendence < 75 :

  print("you are not allowed to sit in the class:")

 else :

  print("You are allowed to sit in the exam")
'''
9.
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

'''
# done upper side

#another ifelse examples
a=int(input("enter the integer"))
if 