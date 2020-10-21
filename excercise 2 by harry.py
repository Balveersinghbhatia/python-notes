#excercise 2 - faulty calculator
# Design a calculator which will correctly solve all the problems except
# 45 * 3 = 555 , 56 +9 = 77 , 56 / 6 = 4
# Your program should take the operator and the two numbers as a input from the user
# and then return the result
l1=["+","-","/","*"]
print(l1)
operator = input("Enter the operator from the following:")
var1=int(input("Enter the first interger:"))
var2=int(input("Enter the second interger:"))

if (var1 == 45 or 3) and (var2 == 3 or 45) and operator == "*":
    print("The multiplication of 45 and 3 is 555")
elif (var1 == 56 or 9)and (var2 == 9 or 56) and operator == "+":
    print("The addition of 56 and 9 is 77")
elif (var1 == 56 or 6) and (var2 == 6 or 56) and operator == "/":
    print("The division of 56 and 6 is 4")
else:
    if operator == l1[0]:
        print("The sum of two integer is :",var1 + var2)
    elif operator == l1[1]:
        print("The subraction of two integers {0} - {1} is {2}".format(var1,var2,var1-var2))
    elif operator == l1[2]:
        print("The division of two integers {0} / {1} is {2}".format(var1,var2,var1/var2))
    else:
        print("The multiplicatin of two integers: {0} * {1} is {2}".format(var1,var2,var1*var2))

