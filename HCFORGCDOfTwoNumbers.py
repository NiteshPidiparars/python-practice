'''
Calculation of HCF Using Python: In this video, we will learn to find the GCD of two numbers using Python. 
Python Program to Find HCF or GCD is asked very often in the exams and we will take this up in todays video!
Highest Common Factor or Greatest Common Divisor of two or more integers when at least one of them is not zero is the largest 
positive integer that evenly divides the numbers without a remainder. For example, the GCD of 8 and 12 is 4
'''
num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if num2 > num1:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"The HCF/GCD of these two numbers is {hcf}")
