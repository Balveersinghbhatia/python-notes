
# Dictionary is a data container which has key value pairs
dict1={"key1":"value1",
       "key2":"value2",
       "key3":"value3",
       "key4":"value4",
       "key5":"value5"}
print(dict1)
# Dictionary is enclosed within curly brackets {}
# extracting keys from the dictionary\
print(dict1.keys())
#extracting values from the dictionary
print(dict1.values())
#extracting the value of specify keys
print(dict1["key1"])
#the values of keys can be a dictionary itself or a list or a tuple
dict2={"papa":"Father",
       "mumma":"Mother",
       "behen":"sister", # dictionary as an value
       "bhai":{"saga bhai":"Sibling","chacha ke bhai":"cousing","aur koi bhai":"relative"}}
print(dict2["bhai"]["chacha ke bhai"]) # extracting value of dictionary as an value itself dict ke ander dict
# list as an value
dict3={"kese ho":["thik hu","acha hu","nhi thik nhi hu","okay hu"]}
print(dict3["kese ho"] [::2]) # applying list extracting as value is in list form
# changing the existing value or adding an key : value
dict3["kese ho"]=["thik hu","acha hu","nhi thik nhi hu","okay hu","me toh bot badiya"]
print(dict3) # we changed the value for key
# now adding new key
dict3["muje bhi lo yrr"]="lo le liya" # also this can be used: dict3.update(["muje bhi lelo yrr"]="lo le liya")
print(dict3)
#deleting some existing key:value
del dict1["key5"]
print(dict1)
#practice test by harry
practice_dict={"intrigued":"it means to be intrested by seeing something or someone",
               "dynamic":"not constant",
               "penetration testing":"it means to exploit the weak point to the point we can do",
               "vulnerablity assesment":"to find the vulnerablities in the system and report it",
               "threat":"danger to anything is called threat",
               "asset":"a thing which is gained after breaking/hacking into the system"}
a=str(input("please enter any from the following to know the meaning (intrigued,dynamic,penetration testing,vulnerablity assesment,threat,asset):"))
print(practice_dict[a])


dict4= practice_dict.copy() #copy operator copy the all elementsof a dictionary
print(dict4)
#practice_dict.clear() #clear operator clear the dictionary by removing allobjects
#print(practice_dict)
print(dict4.fromkeys("intrigued")) # i dont get the function will be updated soon
print(dict4.items()) # gives the tuple for every key value pair
print(dict4.get("asset"))