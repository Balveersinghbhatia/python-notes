#function that reverses the string
"""def reversing_string(string):
    a=string
    print(a[::-1])

str1=str(input("please enter the string:"))

reversing_string(str1) """

#now starting the tutorial from here
# list is a data container in which different types of data can
# can be stored together
# it is mutable means editable /changealbe
bani=["japji sahib","jaap sahib","tva prasad saviye","chaupai sahib","anand sahib"
       ,23,2.6,True,4j]
print(bani)
#now extracting elements from the list

print(bani[::-1]) #all rules of string slicing is also applicable to list slicing
print(len(bani))
print(type(bani))
# some functions of list
l1=['hello','world','how','are','you']
l1.sort() # this will sort the list (alphabate wise in our case)
l1.reverse() # this will reverse the list
print(l1)
l2=[45,54,92,15,404,56]
print(max(l2)) # max gives the max number in the list
print(min(l2))#min gives the minimum number in the list

l1.append(32) # append means add in the end so it will add the data at the end of list
bani.insert(2,"dhan guru granth sahib") # insert function is used to insert data at certain index in between
# parameter is (no of index,data)
print(l1 ,bani )
bani.pop() # .pop removes the last member , this will remove the last member of list
print(bani)
bani.remove("dhan guru granth sahib") # .remove function remove the specified member
#we can also modify the existing values
l2[1]="54" #this will change the value of index 1 to "54"
print(l2)
# for changing the values of two variable
x=12
y=23
print(x,y)
x,y=y,x
print(x,y)
print(l1 + l2) #concatinating two lists
print(l1*3) # repeating the list
l9=["hello","how","wher","now",'why']
#l9.clear() # clears the elements of list
#print(l9)
name=l9.copy() # .copy operator is used to copy the elements of the list
print(name)
l6=[1,2,3,3,3,4,4,2,2,3]
print(l6.count(3)) #count operator counts the no of time specified element comes
l9.extend(l6) # this means extend l9 with l6
print(l9)
print(l9.index(3)) # give the index of the element specified

# here are the list of all functions of list
functionsoflist =['len','type','min','max',"append","insert","pop","remove","sort","reverse","extend",
                  "copy","clear","index",'COUNT',"concatenate","repeating"]
print("the list of all functions of list is as follow : " , functionsoflist)