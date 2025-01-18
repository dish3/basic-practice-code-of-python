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