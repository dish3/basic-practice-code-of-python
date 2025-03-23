#simple function code 
'''#simple function code 
def list1():
("enter the list :").split()
def list1():

    print("length of list :",l
en(l1)) 
    print("user inp
ut item :")
    for item in l1:
    

list1()'''

#factorial code with function 
'''n = int(input("Enter a value: "))

def facto():
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is:", fact)

facto()'''

#convert inr to usd 
'''
n = input("Choose conversion (inr to usd / usd to inr): ").strip().lower()
amount = float(input("Enter amount: "))

if n == "inr to usd":
    print(f"{amount} INR = {amount / 86:.2f} USD")
elif n == "usd to inr":
    print(f"{amount} USD = {amount * 86:.2f} INR")
else:
    print("Invalid choice!")'''
'''
    #Write a recursive function to calculate the sum of first n natural no.
n=int(input("enter a no: "))

def recur(n):
    if(n==0):
        return 0
    return recur(n-1)+n

sum=recur(n)
print(sum)'''

#write a recursive function to print all elements in list 
#hint : use list & index as parameters 

n=input("enter a list: ").split()

def recur(n,idex=0):
    if(idex==len(n)):
        return
    print(n[idex])
    recur(n,idex+1)

l=recur(n)





