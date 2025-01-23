#WAP ask the user to enter names of their 3 favorite movies & store them in list 
"""
movie=[] #list 
movie.append((input("enter movie 1: "))) #input
movie.append((input("enter movie 2: "))) #input
movie.append((input("enter movie 3: "))) #input
print(f"you entered : {movie} ") #output

"""

#WAP to check if a list contains a palindrome of elements.
#(Hint: use copy() method)
"""
str= input("enter the elements: ").split() # Split input into a list of strings
str1 = str.copy()  # Create a copy of the original list
str1.reverse() # Reverse the copied list

# Compare the original list with the reversed list
if(str==str1):
    print(f"list is palindrome : {str} ")
else:
    print(f"{str} is not palindrome")
    """

#WAP to count the number of student with "A" grade in the following tuple 
grade=input("enter the grade") # Take input as a string of grades
tuple1= tuple(grade.split()) # Convert the grades into a tuple
print(tuple1.count("A")) # Count occurrences of "A"

#store the above values in a list & sort them from "A" to "D"

list1 = list(grade.split())
list1.sort()

print("sorted list : ",list1) 



