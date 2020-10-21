# SET IS A COLLECTION OF WELL DEFINED OBJECTS
A = set(['a', 4, 'b', 3])  # this is also known as chrome casting
print(type(A))
print(len(A))
print(A)
# SO THIS WERE THE COMMON FUNCTIONS TYPE , LEN , CHROMECAST
# SET IS A UNORDERED COLLECTION OF OBJECTS
# SO NO POINT OF EXTRACTION(SLICING),BECAUSE THERE IS NO CONSTANT INDEXING
# SET ALSO DOESNT TAKE REPETITION OF OBJECTS
# SET IS ALSO ENCLOSED WITHIN CURLY BRACKETS {}
# SOME FUNCTIONS
A.add("hello world")  # adding object
A.remove('a')  # removing object
print(A)
# union and intersection
B = {1, 2, 3, 4}
print(A.union(B))  # union means the addition of objects without repeating
print(A.intersection(B))  # intersection means common objects
print(min(B))
print(max(B))
print(A.isdisjoint(B))
print(
    A.difference(B)
)
print(A.issubset(B))  # subset means all values of a is in b
print(A.issuperset(B))  # superset means is subset with more value

a = set(("hello world", "how are you ", 12, 3, 4, 88))
print(a)  # this is done for showing it is unordered
