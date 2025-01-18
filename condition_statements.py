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
""""
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

    """
#WAP to check if no. entered by user is odd or even
"""
num = int(input("enter the no. : "))
if(num/2==0):
    print(num," is even ")
else:
    print(num," is the odd no.")

    """
#WAP to find the greatest of 3 no. entered by user
"""
a = int(input("enter first no : "))
b = int(input("enter second no. : "))
c = int(input("enter third no. : "))

# Check which number is the largest

if(a>=b and a>=c):
    print("first no. is largest : ",a)
elif(b>=a and b>=c):
        print("The second number is the largest:", b)
elif(c>=a and c>=b):
        print("The third number is the largest:", c)
   
# Check for equality among the numbers

if(a==b==c):
    print("All three numbers are equal.")
    if(a==b==c):
        print("all three are equal")
    elif(a==b):
        print("The first and second numbers are equal.")
    elif(b==c):
        print("The second and third numbers are equal.")
    elif a == c:
        print("The first and third numbers are equal.")


# Display the entered numbers
        
print(f"you entered no. : are \n first no. : {a} \n second no. : {b} \n third no. : {c}")

"""
        
#WAP to check if a no. is a multiple of 7 or not

num = int(input("enter a no.: "))
if(num%7==0):
    print(f"num is multiple to 7 \n num is :{num}")
else:
    print(f"num is not multiple to 7 \n is : {num}")
