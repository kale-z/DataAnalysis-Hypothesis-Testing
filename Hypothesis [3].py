# coding=utf-8
import csv
from math import sqrt
from scipy.stats import norm
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
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


### Third Hypothesis:

"""since the third Hypothesis is (Time Spent VS Gender),
We take the first and third columns, which we need, and get rid of the other columns"""

# Slicing the Data
Data_Third = []
for row in Data:
    Data_Third.append([row[2], row[0]])


# ============================================================================================


## First Hypothesis Testing Method: Difference of Means
## T - Test

## Finding the needed parameters
# Computing the Mean of Males & Females
Males,Females,M_Counter,F_Counter = 0,0,0,0
for pair in Data_Third[1:]:
    if pair[1] == 'M':
        Males += pair[0]
        M_Counter += 1
    else:
        Females += pair[0]
        F_Counter += 1
MalesMean, FemalesMean = (float(Males)/M_Counter), (float(Females)/F_Counter)

# Computing the Variance of Males & Females
MalesVariance, FemalesVariance = 0,0
for pair in Data_Third[1:]:
    if pair[1] == 'M':
        MalesVariance = MalesVariance + (pair[0] - MalesMean)**2
    else:
        FemalesVariance = FemalesVariance + (pair[0] - FemalesMean)**2
MalesVariance, FemalesVariance = float(MalesVariance/M_Counter), float(FemalesVariance/F_Counter)

## Applying the formula steps
Means_Difference = FemalesMean - MalesMean
Standard_Error = sqrt((MalesVariance/M_Counter) + (FemalesVariance/F_Counter))
T_Test = Means_Difference / Standard_Error
PValue = 0.0238


# ============================================================================================


## Second Hypothesis Testing Method: Correlation Coefficient
## R - Value

# Grouping the values By the Gender
Gender_Time = defaultdict(list)
for value, key in Data_Third[1:]: Gender_Time[key].append(value)

# Counting the frequency of values
MFreq = Counter(Gender_Time['M'])
FFreq = Counter(Gender_Time['F'])

# Exceptional Situations:
# if a key doesn't exist in one of the dictionaries, add it from the other dictionary
# and make its value = 0, this means that the student didn't spend that much of time
if len(MFreq) < len(FFreq):
    for key in FFreq:
        if key not in MFreq:
            MFreq[key] = 0
elif len(FFreq) < len(MFreq):
    for key in MFreq:
        if key not in FFreq:
            FFreq[key] = 0

# Then, we need to compute the Correlation Coefficient parameters
# Which are: [sum of: (X), (Y), (X*Y), (X^2), (Y^2)]
X_Sum = sum(MFreq.values())
Y_Sum = sum(FFreq.values())
XY_Sum = sum({k : v * FFreq[k] for k, v in MFreq.items() if k in FFreq}.values())
X_Squared = sum([MFreq[key]**2 for key in MFreq])
Y_Squared = sum([FFreq[key]**2 for key in FFreq])

# Now, implementing the Correlation Coefficient Formula
R = ((len(MFreq) * XY_Sum) - (X_Sum * Y_Sum)) / (sqrt(((len(MFreq) * X_Squared) - (X_Sum ** 2)) * (len(MFreq) * Y_Squared) - (Y_Sum ** 2)))
critic = 0.532


# ============================================================================================

# Plot
plt.figure(1)
plt.plot(np.linspace(-3, 3, 100), norm.pdf(np.linspace(-3, 3, 100), 0, 1))
plt.axvline(T_Test, color='r', linestyle='--', linewidth=1.8)
plt.axvline(-T_Test, color='r', linestyle='--', linewidth=1.8)
plt.axvline(R, color='g', linestyle='-', linewidth=1.5)
plt.axvline(critic, color='c', linestyle='-', linewidth=1.5)
plt.title("Normal Distribution Showing the Rejection Region")
plt.xlabel("Rejection Region                                                                               Rejection Region")
x1 = plt.scatter([],[], s=20, marker='_', color='green')
x2 = plt.scatter([],[], s=20, marker='_', color='c')
x3 = plt.scatter([],[], s=20, marker='_', color='red')
plt.legend((x1,x2,x3),('Correlation Coefficient Value [R]', 'Critical Value', 'T-Test Value'), scatterpoints=1, loc='upper left', fontsize=10)
plt.show()


print("H0: There is NO Significance Difference between Spent Time on social media and students's Gender [H0: P = 0]")
print("H1: There is a Significance Difference between Spent Time on social media and students's Gender [H0: P ≠ 0]\n")
print("## For the First Hypothesis Testing Method Calculations:")
print("     We found that the T-Test value = %f, and after looking at the T-Table, we got the P-Value = %f\n" % (T_Test, PValue))
print("## For the Second Hypothesis Testing Method Calculations:")
print("     We found that the Correlation Coefficient [R] value = %f" % (R))
print("     Then, after looking at the Critic Values Table, we got the value: %f\n" % (critic))
print("Pointing out the parameters: T-Test , R and its critical value on the Normal Distribution graph")
print("The Acceptance Region is the region between the 2 vertical lines (T-Test values), otherwise it is rejected")
print("We can see that our Correlation Coefficient [R], its Critical value and P-Value lay in the Acceptance Region\n")
print("H0: defendant is guilty")
print("H1: defendant is innocent")


# ============================================================================================
# ============================================================================================


# Part [ 2 ] - Regression:
# Correlation Coefficient proof
a1 = list(set(Gender_Time['M']))
a2 = list(set(Gender_Time['F']))
a2.append(0)
plt.figure(2)
plt.scatter(a1,a2, s=50, color=sum([[s] * n for s, n in zip(['blue', 'red'], [8,8])], []), alpha=0.5)
plt.title("Data Distribution of Time Spent on Social Media for [Males vs Females]")
plt.xlabel("Males")
plt.ylabel("Females")
x4 = plt.scatter([],[], s=20, marker='o', color='blue')
x5 = plt.scatter([],[], s=20, marker='o', color='red')
plt.legend((x4,x5),('Males', 'Females'), scatterpoints=1, loc='best', fontsize=15)
plt.show()


# ============================================================================================
# ============================================================================================


