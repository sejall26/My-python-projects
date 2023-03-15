# Function which return reverse of a string
  
def palindrome(name):
    return name == name[::-1]
  
  
# Driver code
name = input("Enter the string: ")
ans = palindrome(name)
  
if ans:
    print("Yes")
else:
    print("No")