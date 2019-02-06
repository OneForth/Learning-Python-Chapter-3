#Filename: Ch3-5.py
#Author: OneForth
#Last Modified: Febuary 5, 2019
#Converts Fahrenheit to Celsius and Visa Versa


#   Assigning two variables, one int and one str
temp_input = 0
repeat = ""

#   Assigning function for time conversion
def temp_conversion():
    #   Boolean to keep while loop looping until changed to false
    looping = True
    while looping == True:
        #   Displays options to the user
        print("This program will convert Celsius to Fahrenheit and vise versa."
              "\nEnter 1 for Celsius to Fahrenheit,"
              "\nor "
              "\nEnter 2 for Fahrenheit to Celsius.")
        #   Prompts user to input their selection
        option = eval(input("Please selection an option: "))
        #   Celsius to Fahrenheit conversion
        if option == 1:
            #   Prompt user to input temperature in Celsius to convert
            temp_input = eval(input("Please enter the temp: "))
            #   Reports the results
            print(temp_input * 9 / 5 + 32)
        #   Fahrenheit to Celsius conversion
        elif option == 2:
            #   Prompts user to input temperature in Fahrenheit to convert
            temp_input = eval(input("Please enter the temp: "))
            #   Reports the results
            print(5 / 9 *(temp_input - 32))
        #   Prompts the user to input weather they want to continue or not
        repeat = input("Would you like to convert another tempature? Yes or No: ")
        #   Checks for list elements below in users input, will run if there a match
        if repeat in ["NO", "No", "no", "nO"]:
            #   Changes looping boolean breaking out of while loop
            looping = False
#   Calls functions
temp_conversion()
