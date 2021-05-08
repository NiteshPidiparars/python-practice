'''
In this tutorial, we are going to learn how to create a store calculator and receipt generator using python.  
We are going to be using Pycharm IDE for this project. So we have to create an application which will take input from the user and add it until the user presses his enter key and then display the total price. 
Watch the video for better understanding of this project. 
This is a basic application whih can be used in stores to calculate and generate bill. 
This application will keep store the numbers user has put and will add them until the user presses "q" on their keyboard. Then the application will print the result as a bill. 
'''
sum = 0
while (True):
    userInput = input("Enter the item price or press q to quit: \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us")
        break
