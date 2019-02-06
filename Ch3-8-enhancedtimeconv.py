# Filename: Ch3-8-enhancedtimeconv.py
# Author: OneForth
# Last Modified: Febuary 5, 2019
# Advanced Version
# Converts seconds into hours, minutes and remander seconds
# With 1: 34: 05 type of format instead of 1 Hrs 34 Mins 24 Secs

#   Seconds input from user
seconds = eval(input("please enter the amount of seconds: "))
#   Here we compute the amount of hours frm the given seconds
hours = seconds // 3600
#   Compute the remainder of seconds
seconds = seconds % 3600
#   Compute the amount of minutes with the remainder of the seconds
minutes = seconds // 60
#   Compute the final amount of seconds
seconds = seconds % 60
#   Reports the results
print(hours, ":", sep="", end=" ")
#   Computes tens digit for minutes
tens = minutes // 10
#   Compute ones digit for minutes
ones = minutes % 10
#   Reports the results
print(tens, ones, ":", sep="", end=" ")
#   Computes the tens for seconds
tens = seconds // 10
#   Computes the ones for seconds
ones = seconds % 10
#   Reports the final end of the result
print(tens, ones, sep="")


