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

marks = int(input("enter marks : "))

if(marks>=90):
    print("A")
elif(90> marks >= 80):
    print("B")
elif(80> marks >= 70):
    print("C")
else:
    print("D")