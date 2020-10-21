#string slicing means extracting characters from the indexing
str1="hello world"
#     012345678910
print(str1[0]) #indexing starts from zero
print(str1[1:5]) #for extracting some middle words
print(str1[-1]) #-1 is used for last character
print(str1[3:10]) # when in extracting some middle words last is not printed
print(str1[3:-1]) # same as above
print(len(str1)) # len() gives the lenght of string
print(str1[1:11]) # if we want add the last character just add one to index
print(str1[0:]) #if we have left the right side it will counts as lenght of string
print(str1[:5]) # if we have left the  left side it will counts as zero

#ADVANCED SLICING
print(str1[0:7:2]) # imp # second colum is used for specifiying for skipping the letters
print(str1[::]) # by default if nothing is given third colum is considered as one
print(str1[-9: -3]) # negative indexing starts from -1 and from the last character
print(str1[::-1]) # this will reverse the string as it is starting the string from last
#SOME STRING FUNCTIONS
print(str1.endswith("d")) # endswith fucntion check if the string ends with given character or not
print(str1.count("l")) # count fucntion counts the given character in the string
print(str1.capitalize()) # capitalize function will capitalize the first character(only)
print(str1.upper()) # .upper() will uppercase all the characters
print(str1.lower()) # lower() will lowercase all the characters
print(str1.find("l")) # .find() fucntion  will find the character by index
print(str1.replace("world","universe")) # .replace function will replace the word with given word

str2="are kese ho app log i am thinking that you are FINE    "
print(str2.title()) # capitalize the first letter of every word
print(str2.startswith("are")) # opposite to ends with
print(str2.swapcase()) # swap lower character with upper are vice versaa
functionsofstring = ["endswith","count","title","capitalize","upper","lower","find",
                     "replace","startswith","swapcase"]
print("the functions of string we know are:",functionsofstring)