'''
In this tutorial, we are going to learn how to calculate the factorial of a given number and also we are going to find the number of trailing zeroes in that number.
Now let's see what a Factorial is. A factorial is a function that multiplies a number by every number below it. 
For example 7!= 7*6*5*4*3*2*1=5040.
Now to generate the factorial of a given number we are going to be using the recursive approach because it is easy. 
We are going to create a class as factorial() and put a recursive function there to calculate the factorial.Now to find the number of trailing zeroes of that factorial, we are going be using a while loop, 
where we will count the numbers and then return the trailing zeroes of that factorial number. 
For better understanding the video
'''


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


def factorialTrailingZeroes(number):
    #fac = factorial(number)
    # print(fac)
    count = 0
    i = 5
    while (number//i != 0):
        count += int(number/i)
        i = i*5
    return count
    # while (fac%10 ==0):
    #count = count+1
    #fac = fac/10
    # return count


if __name__ == '__main__':
    number = int(input("Enter a number: \n"))
    #fac = factorial(number)
    #print(f'The factorial is {fac}')
    print(factorialTrailingZeroes(number))
