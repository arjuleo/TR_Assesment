# Program : How to Calculate a simple interest

import math

# Input

P= float(input("Enter the principal amount in rupees : "))
T= float(input("Enter the tenure in months : "))
R= float(input("Enter the annual rate of interest : "))

# Process

t=T/12

SI = (P*t*R)/100

# Output
               
print("The simple interest per month is %0.2f rupees" % SI)


            


