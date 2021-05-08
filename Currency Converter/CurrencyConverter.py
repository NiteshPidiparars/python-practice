'''
In this tutorial we are going to create a python currency converter application.First go to this website and copy the data. 
After copying the data past it inside a text file and then fire up your favourite IDE.
Now let's create our program by making a main.py file. In order to make this application work, 
we need to open the txt file and then we have to get the predefined values in a dictionary so we can use them to convert. 
we have to take input from the user and convert it to the users desirable currency. For better understanding you can watch the video
'''
with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(
    f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
