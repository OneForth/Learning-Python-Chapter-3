#Filename: Ch3-1-adder.py
#Author: OneForth
#Last Modified: Febuary 6, 2019



print("This program will add two numbers together of your choice and print out the sum.\nLets begin!")
#Just a print statment letting the user know what this program is for.


value1 = eval(input("Please enter a number: "))
value2 = eval(input("Please enter another number"))
#Gathers input from the user using an input function inside a eval fuction

print(value1, "+", value2, "=", value1 + value2)

