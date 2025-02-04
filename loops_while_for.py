#print number from 1 to 100
"""
i = 0
while i<=100:
    i+=1
    print(i) """

#print number from 100 to 1
"""
i=101
while i>=1:
    i-=1
    print(i)
    """
#print the multipication table of a number n
"""
n= int(input("enter a no: "))
i=1
while i<=10:
    print(f"{n}x{i}= {n*i}")
    i+=1
 """ 
#print the elements of the following list using a loop:
"""
list1=[1,4,9,16,25,36,49,64,81,100]
ind=0
while ind < len(list1):
    print(list1[ind])
    ind += 1
"""
#search for a number x in this tuple using loop
list1=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the no: "))
i=0
found=False
while i< len(list1):
    if(list1[i]==x):
        print(f"found {i}")
        found = True
        break 
    i+=1

if not found:
        print("not found")
   