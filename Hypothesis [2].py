# coding=utf-8
import csv
from math import sqrt
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

"""To find if there is a correlation between the Hypothesis variables
I will use the formula of Correlation Coefficient on the given Sample Data"""

Data = []  # Creating a list to contain the Data
# Importing Data from Excel file
with open('data.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Data.append(row)
# Since the imported Data values are strings, convert them to integers
for i in range(len(Data) - 1):
    Data[i + 1][1], Data[i + 1][2], Data[i + 1][3] = int(Data[i + 1][1]), int(Data[i + 1][2]), float(Data[i + 1][3])


# ============================================================================================
# ============================================================================================


### Second Hypothesis:

"""since the second Hypothesis is (Time Spent VS Age),
We take the second and third columns, which we need, and get rid of the other columns"""

# Slicing the Data
Data_Second = []
for row in Data:
    Data_Second.append([row[2], row[1]])

# Then, we need to compute the Correlation Coefficient parameters
# Which are: [sum of: (X), (Y), (X*Y), (X^2), (Y^2)]
X, Y, XY_Parameter, Xsquared_Parameter, Ysquared_Parameter = 0, 0, [], [], []
for row in Data_Second[1:]:
    X, Y = X + row[0], Y + row[1]
    XY_Parameter.append(row[0] * row[1])
    Xsquared_Parameter.append(row[0] ** 2)
    Ysquared_Parameter.append(row[1] ** 2)
XY, Xsquared, Ysquared = sum(XY_Parameter), sum(Xsquared_Parameter), sum(Ysquared_Parameter)

# Now, implementing the Correlation Coefficient Formula
R = ((len(Data_Second[1:]) * XY) - (X * Y)) / (sqrt(((len(Data_Second[1:]) * Xsquared) - (X ** 2)) * (len(Data_Second[1:]) * Ysquared) - (Y ** 2)))
critic = 0.197 # Getting this value from the Critical Values table

# Plot
# Testing the Correlation Coefficient (R)
plt.figure(1)
plt.plot(np.linspace(-3, 3, 100), norm.pdf(np.linspace(-3, 3, 100), 0, 1))
plt.axvline(critic, color='r', linestyle='--', linewidth=1.8)
plt.axvline(-critic, color='r', linestyle='--', linewidth=1.8)
plt.axvline(R, color='g', linestyle='-', linewidth=1.5)
plt.title("Normal Distribution Showing the Rejection Region")
plt.xlabel("Rejection Region                        Rejection Region")
x1 = plt.scatter([],[], s=20, marker='_', color='green')
x2 = plt.scatter([],[], s=20, marker='_', color='red')
plt.legend((x1,x2),('Correlation Coefficient Value [R]', 'Critical Value'), scatterpoints=1, loc='upper left', fontsize=10)
plt.show()

print("H0: There is NO Significance Correlation between Spent Time on social media and students's AGE [H0: P = 0]")
print("H1: There is a Significance Correlation between Spent Time on social media and students's AGE [H0: P ≠ 0]\n")
print("After all the calculations, we found that the Correlation Coefficient [R] value = %f" % (R))
print("Then, after looking at the Critic Values Table, we got the value: %f" % (critic))
print("Pointing out the R and Critic value on the Normal Distribution graph")
print("We found that R does not fall into the Rejection Region, which is above %f This means: \n" %(critic))
print("H0: defendant is guilty")
print("H1: defendant is innocent.")


# ============================================================================================
# ============================================================================================


# Part [ 2 ] - Regression:
# Correlation Coefficient proof
colors = np.random.rand(len(Data_Second[1:]))
area = np.pi * (15 * np.random.rand(len(Data_Second[1:])))*2
plt.figure(2)
plt.scatter([row[0] for row in Data_Second[1:]], [row[1] for row in Data_Second[1:]], s=area,c=colors, alpha=0.5)
x=[pair[0] for pair in Data_Second[1:]]
y=[pair[1] for pair in Data_Second[1:]]
m, b = np.polyfit(x,y, 1)
Xnew = []
for i in range(len(x)):
    Xnew.append((x[i] * m)+b)
plt.plot(x, Xnew,'c-')
plt.title("Data Distribution for [Time Spent vs Student's Age]")
plt.xlabel("Time Spent on Social Media")
plt.ylabel("Age of students")
plt.show()


# ============================================================================================
# ============================================================================================

