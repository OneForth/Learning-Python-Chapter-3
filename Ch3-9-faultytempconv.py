# Filename: Ch3-9-faultytempconv.py
# Author: OneForth
# Last Modified: Febuary 6, 2019
# Converts Fahrenheit to Celsius
# Results will be the same everytime because degF is equal to zero when used in degC


#   Make some variables
degF, degC = 0, 0
#   Define relationship between F and C
degC = 5/9*(degF - 32)
#   Prompt user for temperature to convert and read the supplied value
degF = eval(input("Plase enter temp in degrees F: "))
#   Report the results
print(degF, "Degrees F = ", degC, "Degrees C")