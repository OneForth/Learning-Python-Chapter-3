# Filename: Ch3-7-timeconv.py
# Author: OneForth
# Last Modified: Febuary 5, 2019
# Converts seconds into hours, minutes and remander seconds

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

#   Reports the results back to the user
print(hours, "Hrs", minutes, "Mins", seconds, "Secs")
