#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 Solutions

# #### 1.Write a Python program to convert Kilometers to Miles ?

# In[1]:


def kmToMiles():
    kiloMeters = float(input("Enter no of kilometers : "))
    print("{} km is Equal to {} miles".format(kiloMeters,kiloMeters*0.621))

kmToMiles()


# #### 2.Write a Python program to convert Celsius to Farenheit ?

# In[2]:


def celToFarh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
celToFarh()


# #### 3.Write a Python program to display calender ?

# In[3]:


import calendar

def showCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
showCalender()


# #### 4.Write a Python program to solve quadartic equation ?

# In[4]:


import cmath
import math

def quadarticEquationRoots(a,b,c):
    
    discriminant = b*b-4*a*c
    
    if discriminant == 0:
        r1 = -b/2*a
        r2 = -b/2*a
        print("Roots are Real",r1,r2)
    elif discriminant > 0:
        r1 = (-b-math.sqrt(discriminant))/(2 * a)
        r2 = (-b+math.sqrt(discriminant))/(2 * a)
        print("Roots are Real and different",r1,r2)
    else:
        r1 = (-b-cmath.sqrt(discriminant))/(2 * a)
        r2 = (-b+cmath.sqrt(discriminant))/(2 * a)
        print("Roots are Imaginary",r1,r2)


a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

quadarticEquationRoots(a,b,c)


# #### 5.Write a Python program to swap two variables without temp variable ?

# In[5]:


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


def swapNumbers(num_1,num_2):
        print('Before Swapping',num_1,num_2)
        num_1 = num_1+num_2
        num_2 = num_1-num_2
        num_1 = num_1-num_2
        print('before Swapping',num_1,num_2)

swapNumbers(num_1,num_2)

