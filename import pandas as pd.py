import pandas as pd
import math


sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0

dt = pd.read_excel(r'C:\Users\91746\Documents\record1.xlsx')
print(dt)

# salary-------------------------------
l1 = dt['Salary(y)'].tolist()
t1 = len(l1)
print("Salary")

# sum of salary------------------------
print(l1)
for i in range(0, t1):
    sum0 = sum0 + l1[i]
print("\nSum of Salary", sum0)

# increment--------------------------------
l2 = dt['Increment(x)'].tolist()

print("\nIncrement")

print(l2)

# sum of increment-----------------------------------
for i in range(0, t1):
    sum1 = sum1 + l2[i]
print("\nSum of Increment", sum1, "\n")

# increment2-------------------------------------------
append1 = []
for i in range(0, t1):
    increment_2 = math.pow(l2[i], 2)
    print("square of increment of", l2[i], "is", increment_2)
    append1.append(increment_2)

# sum of increment 2---------------------------
len1 = len(append1)
for i in range(len1):
    sum2 = sum2 + append1[i]
print("\nThe sum of increment 2", sum2, "\n")

# increment* salary------------------------------------

append2 = []
for i in range(t1):
    increment_X_salary = l2[i] * l1[i]
    print("The salary", l1[i], " * increment is", l2[i], increment_X_salary)
    append2.append(increment_X_salary)

# sum of increment_X_salary-----------------------------------

len2 = len(append2)
for i in range(t1):
    sum3 = sum3 + append2[i]
print("\nThe sum of increment_X_salary", sum3)

# sum of salary(y) is sum0--------------------------
# sum of increment(x) is sum1-----------------------
# sum of increment square(x2) is sum2---------------------
# sum of increment X salary(xy) is sum3--------------------


# Accepting user input-------------------------------------
n = int(input("\nEnter the no. unto which to be checked:\t"))

# printing a-------------------------------
a = ((sum0 * sum2) - (sum1 * sum3)) / ((n * sum2) - (sum2*sum2))

print(a)

# printing b------------------------------------------
b = ((n*sum3)-(sum0*sum1)) / ((n * sum2) - (sum2*sum2))
print(b)