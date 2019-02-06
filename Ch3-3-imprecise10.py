# Filename: Ch3-5.py
# Author: OneForth
# Last Modified: Febuary 6, 2019
# Illustrates how even non-repeatng fractions can be problematic

one = 1.0
one_tenth = 1.0/10.0
zero = one - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth - one_tenth

print("one = ", one, "one_tenth = ", one_tenth, "zero = ", zero)