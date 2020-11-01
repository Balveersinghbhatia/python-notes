for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
print()
for i in range(4): # 0,1,2,3
    for j in range(i+1):
        print("*", end=" ")
    print()
print()
for i in range(4): # 0,1,2,3
    for j in range(4-i):# 4-0=4, 4-1=3,4-2=2,4-3=3,4-4=0
        print("*", end=" ")
    print()

print("new")
for l in range(5):     #0,1,2,3,4,5,6,7,8,9,10
    for j in range(l):#1,2,3,4,5,6,7,8,9,10,11
        print("*",end="")

    print()

for l in range (5):
    for j in range(5-l):
        print("*",end="")

    print()

'''7. Write a Python program that prints each item 
and its corresponding type from the following list.
Sample List : 
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
           [5, 12], {"class":'V', "section":'A'}]'''
l1=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
           [5, 12], {"class":'V', "section":'A'}]
for i in l1:
    print(i,"it type is :",type(i))

'''8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5 '''
for i in range(7):
    if i==3 or i == 6:
        continue
    print(i)

'''9. Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34'''
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y

'''10. Write a Python program which iterates the integers from 1 to 50.
 For multiples of three print "Fizz" instead of the number and for the 
 multiples of five print "Buzz". For numbers which are multiples of both
  three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz'''
print("new line")
for i in range(51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        continue
    if i%3==0:
        print("fizz")
        continue
    if i%5==0:
        print("buzz")
        continue

    print(i)
