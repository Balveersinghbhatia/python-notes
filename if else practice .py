 #Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input("Enter the lenght of quadrilateral:"))
breadth = int(input("Enter the breadth of quadrilateral:"))

if length == breadth :
 print("The quadrilateral is a square")
else:
 print('The quadrilateral is \' only   a rectangle  ')

# Take two int values from user and print greatest among them.
int1 = int(input("Enter the first integer:"))
int2 = int(input("Enter the second integer:"))

if int1 > int2:
 print("The bigger integer is {0}".format(int1))
elif int2 > int1:
 print("The bigger integer is {0}".format(int2))
else:
 print('Both are equal')

'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''
quantity=int(input("Enter the no of units you have bought:"))
totalcost=quantity*100
if totalcost >= 1000 :
 print("The total cost is {0}".format(totalcost - (.1*totalcost )))
else :
 print("The total cost is {0}".format(totalcost))

'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
year_of_service=int(input("Enter the no of years you are working with us:"))
if year_of_service >=16 :
 print("Are you mad or what the company is only 15years old")
else:
  if year_of_service > 5:
   salaryamount = int(input("Enter the your salary amount:"))
   print("you have got bonus of ",.05* salaryamount)
  else:
   print("Sorry to say you will don't have any bonus this year ")
