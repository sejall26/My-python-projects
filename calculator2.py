# Python program to make a simple calculator
def add(X, Y):    
   # Function for adding two numbers   
   return X + Y  
def subtract(X, Y):   
   # Function for subtracting two numbers   
   return X - Y  
def multiply(X, Y):   
   # Function for multiplying two numbers   
   return X * Y   
def divide(X, Y):   
   # Function for dividing two numbers    
   return X / Y   
 
# Taking inputs from user   
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input") 