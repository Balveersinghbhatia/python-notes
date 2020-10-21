
a = 12
b=34
c=int(input("please enter the third integer:"))

print("Now you will get the answer")

if a>b & a>c: # here & , and are same
 print(" {0} is the biggest".format(a))
elif b>a and b>c:
 print(" {0} is the biggest number".format(b))
else:
 print("{0} is the biggest".format(c))

#if else no 2
str1=str(input("Please enter your sirname :"))
print(str1)
if str1=="bhatia":
 print("you are allowed to enter")
else:
 print("you are not allowed to enter")


#now what is differnce between using many if's and using elif
#if we know that the probablity of event is not many
#than we use elif instead of many if's
#but if we don't know than many if's instead of elif


#two operators in and not in
l1=[1,2,34,4,5]
if 1 in l1 : # in operator is used to check if object is there 2
 print("it is true")
if 33 not in l1: # not in operator is used to check if object is not there
 print("it is true ")
# task given by harry
age=int(input("Please enter your age:"))
if age > 6 and age < 80:
 if age > 18:
  print("You are allowed to drive the car")

 elif age == 18:
  print('''Please come to us we will check you physically and say if you
       are allowed or not''')

 else:
  print("You are not allowed to drive a car")
else:
 print("you are not in this program")

