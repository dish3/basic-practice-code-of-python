#conditon statement 
#syntax 
"""
if - elif- else

if(condition): 
    code
elif(condition):
    code
else:
    code

"""
#example 
"""
marks = int(input("enter marks : "))

if(marks>=90):
    print("A")
elif(90> marks >= 80):
    print("B")
elif(80> marks >= 70):
    print("C")
else:
    print("D")

"""
# if-if-elif-else

age= int(input("enter your age : "))

license = input("yes or no : ")

if(80> age >=18):
    if(license== "yes"):
        print("you can drive")
    elif(license== "no"):
        print("you can't drive")
    else:
        print("invalid input for license")
else:
    print("incorrect information filled")
