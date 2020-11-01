# iterate means to do something over again and again or repeatedly
a= "hello world how are you "
for j in a :
    print(j) # so here every word in a is reapiting
l1 = [["jassi",25],["bali",24],["mummy",45],["papa",47]]
for name, age in l1:
    print("The age of {0} IS {1} ".format(name,age))

# quiz given by harry
# we have to create a list
# we have to print only the int objects which is bigger than 6
l2= ["hello world ","how are you",1,2,3, 55,56, 88]

for (j) in l2:
    if  str(j).isnumeric():
        if j > 6:
            print(j,"is int and bigger than 6 ")
        else:
            print(j,"is int but not bigger than 6")
    else:
        print(j,"is not int")

# for loop with single word string
b="now"
for hello in "now":
    print(hello)

#new
avialable = 10
wanted=int(input("how many candies do you want?"))
i=1
while i <= wanted:
    if i > avialable:
        break
    print("candies")
    i += 1
'''Now the difference between pass and continue is that pass statement does nothing where as continue statement skip and goes to next iteration
For example if there are line of code after pass in the if statement they will be printed but in the case of continue it will be not printed
and skipped to next iteration 


Yes, they do completely different things. pass simply does nothing, while continue goes on with the next loop iteration. In your example, the difference would become apparent if you added another statement after the if: After executing pass, this further statement would be executed. After continue, it wouldn't.

>>> a = [0, 1, 2]
>>> for element in a:
...     if not element:
...         pass
...     print element
... 
0
1
2
>>> for element in a:
...     if not element:
...         continue
...     print element
... 
1
2

taken by stack overflow

'''