# Filename: Ch3-6-tempcon.py
# Author: OneForth
# Last Modified: Febuary 6, 2019
# Converts Fahrenheit to Celsius


#   Prompt user for temperature to convert and read the supplied value
degF = eval(input("Plase enter temp in degrees F: "))
#   Convert the temperature
degC = 5/9*(degF - 32)
#   Report the results
print(degF, "Degrees F = ", degC, "Degrees C")