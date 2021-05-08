'''
How to find LCM of two numbers: Today we will write a Python program to find the LCM of two numbers. 
This is a Python Program to find the LCM of two numbers with complete explanation. 
The program takes two numbers and prints the LCM of two numbers.
'''
a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))

maxNum = max(a, b)
while(True):
    if(maxNum % a == 0 and maxNum % b == 0):
        break
    maxNum = maxNum + 1
print(f"The LCM of {a} and {b} is {maxNum}")
