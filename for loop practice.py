'''1. Write a Python program to find those numbers which are
 divisible by 7 and multiple of 5, between 1500 and 2700 (both included).'''
for i in range(1500,2700):
    if i%7 == 0 and i%5 == 0:
        print(i)

'''

2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :                                 #c    (f - 32)
                                                   - =    _
                                                   5      9 
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''


temp=input("please enter the temperature you want to convert:")
degree = int(temp[0:-1])
type=temp[-1]

if type.upper() =="F":
    converted= int(round(5/9 * (degree - 32)))
    print("The conversion of F into C is",converted)
elif type.upper() == "C":
    converted = int(round((9/5) * degree  + 32))
    print("The conversion of c into f is", converted)
else:
    print("please enter proper input")

'''3. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess,
user will get a "Well guessed!" message, and the program will exit.'''
import random

def reverse(string):
    a = string
    print(a[::-1])
str1=str(input("please enter a string"))
reverse(str1)

TUP1=list(int(input("enter a series of number")))
even_numbers= 0
odd_numbers = 0
for i in TUP1:
    print(i)
    if i % 2 == 0:
        even_numbers += 1
    else :
        odd_numbers += 1

print("even numbers are",even_numbers)
print("odd numbers are",odd_numbers)