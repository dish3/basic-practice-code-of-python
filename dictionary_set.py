# store following word meaning in python dictonary 
"""
dictionary={
    "cat":"a small animal",
    "table":{"a piece of furniture", "list of facts & figures"}
}
print(dictionary)
"""

#you are given a list of subject for students. Assume one classroom is requried for 1 subject. how many classroom are needed by all students.
"""
subjects={
    "python","java","c++","python","js","java","python","java","c++","c"
}
print(len(subjects))
"""
#WAP to enter marks of 3 subjects from the user and store them in dictionary. 
#start with an empty dictionary & add one by one. Use subjects name as key & marks as value 
"""
Dict ={}
print(type(Dict))

x= int(input("enter phy :"))
Dict.update({"phy":x})

x= int(input("enter math :"))
Dict.update({"math":x})

x= int(input("enter chem :"))
Dict.update({"chem":x})

print(Dict)

"""
#figure out way to store 9 & 9.0 as seprate values in the set.
#(you can take help of built-in data types)
"""
sets= {}

x= int(input("enter a value "))
sets.update("int":x)

y= float(input("enter a value "))
sets.update("float":y)

print(sets)
"""
#OR
"""
value = {
("float",9.0)
("int",9)
}
print(value)
"""