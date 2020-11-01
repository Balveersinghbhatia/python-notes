# #  for doing something same again and again we use loop statements
# # syntax of while :
# # while condition:
# #    statements
# #    increasemetn/decreasement (end)
#
# i = 0
# while i<10:
#     print("*")
#     i = i + 1
#
# #while loop  practice
# '''
# 1.Take 10 integers from keyboard using loop and print their average value on the screen.
# '''
# i= 10
# sum = 0
# while i > 0:
#     number= int(input("Please enter the integer"))
#     sum = sum + number
#     i -= 1
# average = sum / 10.0
#
# print("average is ",average)
#
# #print following patters
# i = 1
# while i < 5:
#     print("#"*i)
#     i += 1
#
# i = 1
# while i < 11:
#     print(24,"into",i,"=",24*i)
#     i = i + 1

 #  write a infinite loop
# while True :
#      print("kem palty")

# program using while to calculate the factorial
i = int(input("enter the integer"))
j = 1
while j < i:
    print